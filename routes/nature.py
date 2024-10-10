from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user
from database.models.nature import Nature
from database.models.user import User

nature_route = Blueprint('nature', __name__)

'''
    - /nature/                 (GET) Renderizar um formulário para criar um nature
    - /nature/                 (POST) Insere um nature
    - /nature/all              (GET) Listar os natures
    - /nature/<id>             (GET) Obter os dados de um nature   
    - /nature/<id>/edit        (GET) Renderizar um formulário para editar um nature
    - /nature/<id>/update      (PUT) Atualizar os dados de um nature
    - /nature/<id>/warning     (GET) Renderizar um formulário para editar um nature
    - /nature/<id>/delete      (DELETE) Deleta o registro do nature  
'''

@nature_route.route('/', methods=['GET', 'POST'])
def render_form():
    if not current_user.is_authenticated:
        return redirect(url_for('user.login'))
    from forms.nature import NatureForm
    form = NatureForm()
    
    if form.validate_on_submit():
        form.save()
        natures = Nature.select().where(Nature.id_user == current_user)
        return render_template('natures_list.html', natures=natures) 

    return render_template('form_nature.html', form=form)


@nature_route.route('/all', methods=['GET'])
def list_natures():
    if not current_user.is_authenticated:
        return redirect(url_for('user.login'))
    
    natures = Nature.select().where(Nature.id_user == current_user)
    return render_template('natures_list.html', natures=natures)


@nature_route.route('/<int:id_nature>/edit')
def edit_nature(id_nature):
    if not current_user.is_authenticated:
        return redirect(url_for('user.login'))
    from forms.nature import NatureForm
    form = NatureForm()
    nature = Nature.get_by_id(id_nature)
    return render_template("form_nature.html", form=form, nature=nature)


@nature_route.route('/<int:id_nature>/update', methods=['PUT'])
def update_nature(id_nature):
    if not current_user.is_authenticated:
        return redirect(url_for('user.login'))
    from forms.nature import NatureForm
    form = NatureForm()
    
    if form.validate_on_submit():
        natures = Nature.select().where(Nature.id_user == current_user)
        form.edit_save()
        return render_template('natures_list.html', natures=natures)


@nature_route.route('/<int:id_nature>/warning')
def warning_nature(id_nature):
    if not current_user.is_authenticated:
        return redirect(url_for('user.login'))
    nature = Nature.get_by_id(id_nature)
    return render_template("nature_delete.html", nature=nature)


@nature_route.route('/<int:id_nature>/delete', methods=['DELETE'])
def delete_nature(id_nature):
    if not current_user.is_authenticated:
        return redirect(url_for('user.login'))
    
    nature_delete = Nature.delete().where(Nature.id_user == current_user).where(Nature.id == id_nature)
    nature_delete.execute()
    
    natures = Nature.select().where(Nature.id_user == current_user)
    return render_template('natures_list.html', natures=natures)
