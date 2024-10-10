from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user
from database.models.nature import Nature

control_route = Blueprint('control', __name__)

'''
    - /control/                 (GET) Renderizar um formulário para criar um controle
    - /control/                 (POST) Insere um controle
    - /control/all              (GET) Listar os controles
    - /control/<id>             (GET) Obter os dados de um controle   
    - /control/<id>/edit        (GET) Renderizar um formulário para editar um controle
    - /control/<id>/update      (PUT) Atualizar os dados de um controle
    - /control/<id>/delete      (DELETE) Deleta o registro do controle 
    - /control/<id>/estimates   (GET) Lista todos as estimativas para o controle específico 
    - /control/<id>/moves       (GET) Lista todos os movimentos para o controle específico 
'''

@control_route.route('/', methods=['GET', 'POST'])
def render_form():
    if not current_user.is_authenticated:
        return redirect(url_for('user.login'))
    from forms.control import ControlForm
    form = ControlForm()
    
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('home.render_home'))

    return render_template('form_control.html', form=form)

@control_route.route('/<int:id_control>/estimates', methods=['GET'])
def render_nature_list(id_control):
    if not current_user.is_authenticated:
        return redirect(url_for('user.login'))
    from forms.estimate import EstimateForm
    # form = EstimateForm()
    
    # if form.validate_on_submit():
    #     form.save()
    #     return redirect(url_for('home.render_home'))
    
    natures = Nature.select().where(Nature.id_user == current_user)
    forms = []
    for nature in natures:
        form = EstimateForm()
        form.value_nature.label.text = nature.name_nature
        forms.append(form)
    return render_template('natures_estimate.html', forms=forms)