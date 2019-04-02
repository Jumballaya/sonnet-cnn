from flask import Blueprint
import tensorflow as tf
from ml import sonnet_model

graph = tf.get_default_graph()
model = sonnet_model(load=True)

bp = Blueprint('sonnet', __name__)

from app.sonnet import routes
