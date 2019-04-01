'''
Main Routes
'''
from flask import render_template, flash, redirect, url_for, current_app
from app.main import bp



@bp.route('/')
@bp.route('/index')
def index():
    return render_template('main/index.html', title='Home')

@bp.route('/sonnet')
def sonnet():
    with current_app.graph.as_default():
        sonnet = current_app.model.generate(10)
    return render_template('main/sonnet.html', title='Sonnet', sonnet=sonnet)
