from ml import hamspam_model
from ml.models import HamSpamClassifier
from ml.tools import plot_history

def build(text):
    model = HamSpamClassifier('data/spam.csv')
    history = model.train()
    model.save('models/spamham.h5')
    plot_history(history)

def test(text):
    model = hamspam_model()
    res = model.predict(text)
    res = res[0][0]
    if round(res) == 1: print('Spam!')
    elif round(res) == 0: print('Ham!')
    print('Text score: {}'.format(res))


actions = {
    'build': build,
    'test': test,
}
