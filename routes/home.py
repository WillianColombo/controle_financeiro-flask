from flask import Blueprint, render_template

home_route = Blueprint('home', __name__)

@home_route.route('/')
def render_home():
    return render_template('home.html')

@home_route.route('/appbar')
def render_appbar():
    return render_template('appbar.html')