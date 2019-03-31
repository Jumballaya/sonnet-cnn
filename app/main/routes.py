'''
Main Routes
'''
from flask import render_template, flash, redirect, url_for
from app.main import bp
from ml import sonnet_model



@bp.route('/')
@bp.route('/index')
def index():
    return render_template('main/index.html', title='Home')

@bp.route('/sonnet')
def sonnet():
    s_model = sonnet_model(load=True)
    sonnet = s_model.generate(10)
    return render_template('main/sonnet.html', title='Sonnet', sonnet=sonnet)
