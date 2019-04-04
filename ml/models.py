import random
import numpy as np
import pandas as pd
import tensorflow as tf
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, LSTM
from keras.optimizers import Adam
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

'''
Flask Model Wrapper
'''
class FlaskModel(object):

    def __init__(self, name, model):
        self.name = name
        self.graph = tf.Graph()
        with self.graph.as_default():
            self.model = model
            self.session = tf.Session()
            self.saver = tf.train.Saver()
            self.saver.restore(self.session, "models/{}.h5".format(self.name))

    def save(self):
        self.session.run(tf.global_variables_initialize())
        self.saver.save(self.session, "models/{}.h5".format(self.name))

    def predict(self, input_vec):
        result = self.session.run(
            self.model.output_node,
            feed_dict={
                self.model.input_placeholder: input_vec,
            })

        return result




'''
Generic Base Model
'''
class BaseModel(object):
    def __init__(self, name, data):
        self.data = data
        self.model = None
        self.name = name

    def build(self):
        pass

    def train(self, epochs=1, batch_size=1000):
        features = self.data.features
        labels = self.data.labels
        history = self.model.fit(features, labels, epochs=epochs, batch_size=batch_size)
        return history

    def save(self, directory):
        filename = '{}/{}.h5'.format(directory, self.name)
        self.model.save(filename)

    def load(self, directory):
        filename = '{}/{}.h5'.format(directory, self.name)
        self.model = load_model(filename)
        print('Model: {} loaded'.format(self.name))


'''
Chameleon Text Generator.

    Generate text similiar to the given input text
'''
class Chameleon(BaseModel):

    def __init__(self, name, data):
        BaseModel.__init__(self, name, data)

    def build(self):
        if self.model == None:
            features = self.data.features
            labels = self.data.labels
            model = Sequential()
            model.add(LSTM(100, input_shape=(features.shape[1], features.shape[2]), return_sequences=True))
            model.add(Dropout(0.2))
            model.add(LSTM(100))
            model.add(Dropout(0.2))
            model.add(Dense(labels.shape[1], activation='softmax'))
            model.compile(loss='categorical_crossentropy', optimizer='adam')
            self.model = model

    def generate(self, cycles):
        model = self.model
        data = self.data
        string_mapped = data.raw_features[random.randint(1, len(data.raw_features) - 1)]
        full_string = [data.decode[value] for value in string_mapped]

        for i in range(cycles):
            x = np.reshape(string_mapped,(1,len(string_mapped), 1))
            x = x / float(len(data.bank))

            pred_index = np.argmax(model.predict(x, verbose=0))
            pred_index = 1
            seq = [data.decode[value] for value in string_mapped]
            full_string.append(data.decode[pred_index])

            string_mapped.append(pred_index)
            string_mapped = string_mapped[1:len(string_mapped)]

        txt=""
        for char in full_string:
            txt = txt+char

        return txt


class HamSpamClassifier(object):
    def __init__(self, fp):
        self.data = self.get_data(fp)
        self.vectorizer = CountVectorizer(min_df=0, lowercase=False)
        self.vectorizer.fit(self.data['text'])
        self.features = self.vectorizer.transform(self.data['text'])
        self.labels = self.data['category']
        self.model = None
        self.make_model()

    def make_model(self):
        X_train, X_test, y_train, y_test = train_test_split(self.features, self.labels, stratify=self.labels, test_size=0.2)
        input_dim = X_train.shape[1]
        model = Sequential()
        model.add(Dense(10, input_dim=input_dim, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        self.model = model
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test

    def train(self):
        history = self.model.fit(self.X_train, self.y_train, epochs=10, validation_data=(self.X_test, self.y_test), batch_size=10)
        return history

    def save(self, fp):
        self.model.save(fp)

    def load(self, fp):
        self.model = load_model(fp)

    def predict(self, sentence):
        sentence = self.vectorizer.transform([sentence])
        return self.model.predict(sentence)

    def encode_category(self, cat):
        if cat == 'spam': return 1
        else: return 0

    def get_data(self, fp):
        drop_cols = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4']
        df = pd.read_csv(fp, encoding='latin-1')
        df = df.drop(labels=drop_cols, axis=1)
        df.columns = ['category', 'text']
        df['category'] = df['category'].apply(self.encode_category)
        df['length'] = df['text'].apply(len)
        return df
