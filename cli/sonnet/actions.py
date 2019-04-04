from ml import sonnet_model
from ml.tools import plot_history

def build():
    model = sonnet_model()
    history = model.train()
    model.save('models')
    plot_history(history)

def generate():
    model = sonnet_model(load=True)
    print(model.generate(10))


actions = {
    'build': build,
    'generate': generate,
}
