from keras.models import load_model
from keras.applications import ResNet50
from ml.models import Chameleon
from ml.data import TextData


def sonnet_model(load=False):
    data = TextData('./data/sonnets.txt')
    model = Chameleon('sonnet', data)
    if load:
        model.load('models')
    else:
        model.build()
    return model

def imagenet_model():
    return load_model('models/imagenet.h5')
