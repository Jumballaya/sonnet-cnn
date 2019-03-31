import random
import numpy as np
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, LSTM

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
        self.model.fit(features, labels, epochs=epochs, batch_size=batch_size)

    def save(self, directory):
        filename = '{}/{}.h5'.format(directory, self.name)
        self.model.save(filename)

    def load(self, directory):
        filename = '{}/{}.h5'.format(directory, self.name)
        self.model = load_model(filename)


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
            seq = [data.decode[value] for value in string_mapped]
            full_string.append(data.decode[pred_index])

            string_mapped.append(pred_index)
            string_mapped = string_mapped[1:len(string_mapped)]

        txt=""
        for char in full_string:
            txt = txt+char

        return txt


'''
Multivariate Text Classifier

    Classify text as one of the given labels
'''
class Classifier(BaseModel):

    def __init__(self, name, data):
        BaseModel.__init__(self, name, data)

    def build(self):
        if self.model == None:
            features = self.data.features
            labels = self.data.labels
            model = Sequential()
            model.compile(loss='categorical_crossentropy', optimizer='adam')
            self.model = model
