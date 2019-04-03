from keras.models import load_model
from keras.applications import ResNet50, imagenet_utils
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
import numpy as np
from PIL import Image


def prepare_image(image, target):
    if image.mode != 'RGB':
        image = image.convert('RGB')

    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)
    return image

def build(fp):
    model = ResNet50(weights="imagenet")
    model.save('models/imagenet.h5')

def test(fp):
    model = load_model('models/imagenet.h5')
    image = Image.open(fp)
    image = prepare_image(image, (224, 224))
    pred = model.predict(image)
    results = imagenet_utils.decode_predictions(pred)
    print("")
    for (imgID, label, prob) in results[0]:
        print("Label: {}\nProbability: {}\n".format(label, prob))

actions = {
    'build': build,
    'test': test,
}
