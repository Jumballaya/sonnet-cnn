'''
Flask Application Entry
'''
from flask import Flask, request, current_app
from flask_cors import CORS
from app.config import Config


'''
Application creation function
'''
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.sonnet import bp as sonnet_bp
    app.register_blueprint(sonnet_bp, url_prefix='/api/sonnet')

    from app.imagenet import bp as imagenet_bp
    app.register_blueprint(imagenet_bp, url_prefix='/api/imagenet')


    CORS(app)
    return app
