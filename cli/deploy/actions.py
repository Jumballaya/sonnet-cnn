import os

def frontend():
    print('Deploying frontend...')

def models():
    print('Deploying models...')

def services():
    print('Deploying services...')

def database():
    print('Deploying database changes...')

actions = {
    'frontend': frontend,
    'models': models,
    'services': services,
    'database': database,
}
