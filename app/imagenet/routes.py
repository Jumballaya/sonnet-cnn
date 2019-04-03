from flask import jsonify, request
from app.imagenet import bp
from app.imagenet.image import make_prediction


@bp.route('/predict', methods=['POST'])
def predict():
    data = { 'success': False, 'predictions': [] }

    if request.method == 'POST':
        if request.files.get('image'):
            image = request.files['image'].read()
            data['predictions'] = make_prediction(image)
            data['success'] = True

    return jsonify(data)
