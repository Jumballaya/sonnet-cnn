from keras.applications import imagenet_utils
from flask import jsonify, request
from PIL import Image
import io
from app.imagenet import model, graph, bp
from app.imagenet.image import prepare_image


@bp.route('/predict', methods=['POST'])
def predict():
    data = { "success": False }

    if request.method == 'POST':
        if request.files.get('image'):
            image = request.files["image"].read()
            image = Image.open(io.BytesIO(image))
            image = prepare_image(image, target=(224, 224))
            with graph.as_default():
                pred = model.predict(image)
            results = imagenet_utils.decode_predictions(pred)
            data['predictions'] = []
            for (imgID, label, prob) in results[0]:
                r = { "label": label, "probability": float(prob) };
                data['predictions'].append(r)
            data['success'] = True

    return jsonify(data)
