from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
import numpy as np


def prepare_image(image, target):
    if image.mode != 'RGB':
        image = image.convert('RGB')

    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)
    return image
