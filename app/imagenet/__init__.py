from flask import Blueprint
from ml import imagenet_model
import tensorflow as tf

graph = tf.get_default_graph()
model = imagenet_model()

bp = Blueprint('imagenet', __name__)

from app.imagenet import routes
