from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from PIL import Image
import numpy as np
import io
from app.imagenet import model, graph

def make_prediction(img):
    image = Image.open(io.BytesIO(img))
    image = prepare_image(image, target=(224, 224))
    with graph.as_default():
        pred = model.predict(image)
    results = imagenet_utils.decode_predictions(pred)
    data = []
    for (imgID, label, prob) in results[0]:
        r = { 'label': label, 'probability': float(prob) };
        data.append(r)

    return data


def prepare_image(image, target):
    if image.mode != 'RGB':
        image = image.convert('RGB')

    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)
    return image
