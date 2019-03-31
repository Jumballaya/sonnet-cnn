'''
Flask CLI setup

Commands:
    model    -- build or run model
'''
from ml import sonnet_model


def register(app):
    @app.cli.group()
    def model():
        """Work with the model"""
        pass

    @model.command()
    def build():
        """Build the model file"""
        model = sonnet_model(load=False)
        model.train()
        model.save('models')
        pass

    @model.command()
    def generate():
        """Generate a sample"""
        model = sonnet_model(load=True)
        print(model.generate(10))
        print(model.generate(50))
        print(model.generate(100))
        pass
