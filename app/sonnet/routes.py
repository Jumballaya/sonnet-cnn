from flask import jsonify
from app.sonnet import bp, model, graph


@bp.route('/generate')
def generate():
    with graph.as_default():
        sonnet = model.generate(10)
    return jsonify({ 'sonnet': sonnet })
