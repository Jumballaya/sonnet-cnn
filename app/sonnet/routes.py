from flask import render_template, flash, redirect, url_for, current_app
from app.sonnet import bp, graph, model


@bp.route('/generate')
def generate():
    with graph.as_default():
        sonnet = model.generate(10)
    return render_template('sonnet/generate.html', title='Sonnet', sonnet=sonnet)
