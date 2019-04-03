from flask import jsonify
from app.errors import bp

@bp.app_errorhandler(404)
def not_found_error(error):
    return jsonify({
        'code': 404,
        'message': 'Route not found'
    })

@bp.app_errorhandler(500)
def internal_error(error):
    return jsonify({
        'code': 500,
        'message': 'Internal server error'
    })

@bp.app_errorhandler(403)
def forbidden(error):
    return jsonify({
        'code': 403,
        'message': 'Not permitted'
    })
