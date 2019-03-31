import numpy as np
from keras.utils import np_utils

class TextData(object):
    def __init__(self, path, focus='letter', splitText=False, depth=500):
        if focus != 'word': focus = 'letter'
        self.splitText = splitText
        self.depth = depth
        self.focus = focus
        self.path = path
        self.bank = []
        self.encode = {}
        self.decode = {}
        self.features = []
        self.raw_features = []
        self.labels = []
        self.tfeatures = []
        self.tlabels = []
        self.text = ''
        self.process()

    def load_data(self):
        text = open(self.path).read()
        self.text = text.lower()

    def create_mapping(self):
        if self.focus == 'letter':
            self.bank = sorted(list(set(self.text)))
        else:
            self.bank = sorted(list(set((words.lower().split(" ")))))

        self.decode = { n: i for n, i in enumerate(self.bank) }
        self.encode = { i: n for n, i in enumerate(self.bank) }

    def process(self):
        self.load_data()
        self.create_mapping()
        length = len(self.text)
        seq_len = self.depth

        for i in range(0, length - seq_len, 1):
            seq = self.text[i:(i+seq_len)]
            label = self.text[i + seq_len]
            self.features.append([self.encode[char] for char in seq])
            self.labels.append(self.encode[label])

        self.raw_features = self.features
        self.features = np.reshape(self.features, (len(self.features), seq_len, 1))
        self.features = self.features / float(len(self.bank))
        self.labels = np_utils.to_categorical(self.labels)

        if self.splitText:
            if isinstance(self.splitText, int):
                self.tfeatures = self.features[0:self.splitText]
                self.features = self.features[self.splitText:]
                self.tlabels = self.labels[0:self.splitText]
                self.labels = self.labels[self.splitText:]
            else:
                half = int(len(self.features) / 2)
                self.tfeatures = self.features[0:half]
                self.tlabels = self.labels[0:half]
                self.features = self.features[half:]
                self.labels = self.labels[labels:]
