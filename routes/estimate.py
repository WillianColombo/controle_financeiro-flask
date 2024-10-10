from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user
from database.models.nature import Nature

estimate_route = Blueprint('estimate', __name__)

'''
    - /estimate/                 (GET) Renderizar um formulário para criar um estimate
    - /estimate/                 (POST) Insere um estimate
    - /estimate/all              (GET) Listar os estimates
    - /estimate/<id>             (GET) Obter os dados de um estimate   
    - /estimate/<id>/edit        (GET) Renderizar um formulário para editar um estimate
    - /estimate/<id>/update      (PUT) Atualizar os dados de um estimate
    - /estimate/<id>/warning     (GET) Renderizar um formulário para editar um estimate
    - /estimate/<id>/delete      (DELETE) Deleta o registro do estimate
'''

@estimate_route.route('/', methods=['GET', 'POST'])
def render_estimate():
    if not current_user.is_authenticated:
        return redirect(url_for('user.login'))
    from forms.estimate import EstimateForm
    form = EstimateForm()
    
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('home.render_home'))

    return render_template('form_estimate.html', form=form)
