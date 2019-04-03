from flask import Blueprint
from ml import sonnet_model
import tensorflow as tf

graph = tf.get_default_graph()
model = sonnet_model(load=True)

bp = Blueprint('sonnet', __name__)

from app.sonnet import routes
