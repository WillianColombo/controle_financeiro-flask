from flask import Blueprint, render_template

move_route = Blueprint('moves', __name__)

'''
    /move/                      GET - Renderiza os elementos 
    /move/<reference>/          GET - 
'''

@move_route.route('/')
def render_index():
    return render_template('index.html')