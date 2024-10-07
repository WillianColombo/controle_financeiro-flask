from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user

move_route = Blueprint('move', __name__)

'''
    /move/                      GET - Renderiza os elementos 
    /move/control/              GET - Renderiza o formulário de cadastro para novo mês de controle
    /move/control/              POST - Envia o cadastro do formulário para novo mês de controle
'''

@move_route.route('/')
def render_index():
    return render_template('index.html')

@move_route.route('/control', methods=['GET', 'POST'])
def render_control():
    if not current_user.is_authenticated:
        return redirect(url_for('user.login'))
    from forms.control import ControlForm
    form = ControlForm()
    
    if form.validate_on_submit():
            form.save()
            return redirect(url_for('home.render_home'))

    return render_template('form_control.html', form=form)

@move_route.route('/nature', methods=['GET', 'POST'])
def render_nature():
    if not current_user.is_authenticated:
        return redirect(url_for('user.login'))
    from forms.nature import NatureForm
    form = NatureForm()
    
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('home.render_home'))

    return render_template('form_nature.html', form=form)

@move_route.route('/estimate', methods=['GET', 'POST'])
def render_estimate():
    if not current_user.is_authenticated:
        return redirect(url_for('user.login'))
    from forms.estimate import EstimateForm
    form = EstimateForm()
    
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('home.render_home'))

    return render_template('form_estimate.html', form=form)