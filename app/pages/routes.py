from flask import render_template, redirect, url_for
from . import pages_bp
from flask_wtf import FlaskForm
from wtforms import  SubmitField

class HomeID(FlaskForm):
    submit = SubmitField('Submit')

@pages_bp.route('/page-one')
def page_one():
    return "Page One"

@pages_bp.route('/home-id')
def home_id():
    form=HomeID()

    if form.validate_on_submit():
        return redirect(url_for('pages.home_id'))
    return render_template('homeid.html')

@pages_bp.route('/notifications')
def notifications():
    return render_template('Notification.html')

@pages_bp.route('/profile')
def profile():
    return render_template('profile.html')
