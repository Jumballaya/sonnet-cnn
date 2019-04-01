'''
Flask Application Entry
'''
from flask import Flask, request, current_app
import tensorflow as tf
from app.config import Config
from ml import sonnet_model


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

    graph = tf.get_default_graph()
    model = sonnet_model(load=True)
    app.model = model
    app.graph = graph

    return app
