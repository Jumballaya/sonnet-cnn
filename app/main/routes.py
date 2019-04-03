'''
Main Routes
'''
from flask import jsonify
from app.main import bp


@bp.route('/')
def index():
    return jsonify({
        'apis': {
            'sonnet': {
                'generate': '/api/sonnet/generate'
            },
        },
    })
