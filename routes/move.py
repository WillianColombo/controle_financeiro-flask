from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user
from database.models.nature import Nature

move_route = Blueprint('move', __name__)

'''
    /move/nature               GET - Renderiza os campos para cadastro de natureza
    /move/nature               POST - Envia o cadastro do formulário completo para nova natureza
    /move/natures              GET - Renderiza a lista de naturezas cadastradas, a partir do BD
    /move/estimate             GET - Renderiza o formulário de cadastro para a estimativa de gasto da natureza em relação ao controle
    /move/estimate             POST - Envia o cadastro do formulário para a estimativa de gasto da natureza em relação ao controle
'''

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
