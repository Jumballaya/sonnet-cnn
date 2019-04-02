from ml import sonnet_model

def build():
    model = sonnet_model()
    model.train()
    model.save('models')

def generate():
    model = sonnet_model(load=True)
    print(model.generate(10))
