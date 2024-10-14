from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user
from database.models.estimate import Estimate
from database.models.control import Control
from database.models.user import User
from database.models.nature import Nature
from peewee import JOIN

estimate_route = Blueprint('estimate', __name__)

'''
    - /control/<id_control>/estimate/                           (GET) Renderizar um formulário para criar um estimate
    - /control/<id_control>/estimate/                           (POST) Insere um estimate
    - /control/<id_control>/estimate/all                        (GET) Listar os estimates
    - /control/<id_control>/estimate/import                     (GET) Renderiza os controles para importar
    - /control/<id_control>/estimate/import/<id_new_control>    (GET) Importa as estimativas do mês selecionado
    - /control/<id_control>/estimate/adjust                     (GET) Mostra as estimativas em form para alterá-las
    - /control/<id_control>/estimate/adjust/<id_estimate>       (POST) Altera a estimativa específica
    - /control/<id_control>/estimate/<id_estimate>              (GET) Obter os dados de um estimate   
    - /control/<id_control>/estimate/<id_estimate>/edit         (GET) Renderizar um formulário para editar um estimate
    - /control/<id_control>/estimate/<id_estimate>/update       (PUT) Atualizar os dados de um estimate
    - /control/<id_control>/estimate/<id_estimate>/warning      (GET) Renderizar um formulário para editar um estimate
    - /control/<id_control>/estimate/<id_estimate>/delete       (DELETE) Deleta o registro do estimate
'''

@estimate_route.route('/all')
def render_nature_list(id_control):
    if not current_user.is_authenticated:
        return redirect(url_for('user.login'))
    
    results = Estimate.select(
            Estimate.value_estimate, Nature.name_nature).join(
            Control, on=(Estimate.id_control == Control.id)).join(
            User, on=(Control.id_user == User.id)).join(
            Nature, on=(Estimate.id_nature == Nature.id)).where(
            User.id == current_user).where(Control.id == id_control)
    estimates = results.dicts()
    
    return render_template('estimate_list.html', estimates=estimates, id_control=id_control)


@estimate_route.route('/import')
def import_estimates(id_control):
    if not current_user.is_authenticated:
        return redirect(url_for('user.login'))
    
    controls = Control.select().where(
        Control.id_user == current_user).where(
            Control.id != id_control).order_by(
            Control.month_year_control.desc())
    
    return render_template('estimate_import.html', controls=controls, id_control=id_control)


@estimate_route.route('/import/<int:id_new_control>')
def import_estimate_save(id_control, id_new_control):
    if not current_user.is_authenticated:
        return redirect(url_for('user.login'))
    
    # Deleta os registros atuais
    Estimate.delete().where(Estimate.id_control == id_control).execute()
    # Seleciona os novos registros para serem importados
    q = Estimate.select(
        Nature.id.alias('id_nature'),
        Nature.name_nature,
        Estimate.id.alias('id_estimate'),
        Estimate.value_estimate).join(
            Nature, JOIN.RIGHT_OUTER, on=(
                (Estimate.id_nature == Nature.id) & 
                (Estimate.id_control == id_new_control))).where(
            Nature.id_user == current_user)
    new_rows = q.dicts()
    
    # Insere os novos registros
    for row in new_rows:
        Estimate.create(
            value_estimate=row['value_estimate'] if row['id_estimate'] else 0, 
            id_control=id_control, 
            id_nature=row['id_nature'])    
    
    # Seleciona os registros já alterados para serem mostrados na tela
    querry = Estimate.select(
            Estimate.value_estimate, Nature.name_nature).join(
            Control, on=(Estimate.id_control == Control.id)).join(
            User, on=(Control.id_user == User.id)).join(
            Nature, on=(Estimate.id_nature == Nature.id)).where(
            User.id == current_user).where(Control.id == id_control)
    estimates = querry.dicts()
    
    return render_template('estimate_list.html', estimates=estimates, id_control=id_control)
    

@estimate_route.route('/adjust', methods=['GET', 'POST'])
def adjust_estimate(id_control):
    if not current_user.is_authenticated:
        return redirect(url_for('user.login'))
    from forms.estimate import EstimateForm
    
    form_self = EstimateForm()
    if form_self.validate_on_submit():
        if form_self.id_estimate.data:
            form_self.edit_save()
            flash('Estimativa alterada com sucesso!')
        else:
            form_self.save(id_control, form_self.id_nature.data)
            flash('Estimativa salva com sucesso!')
            
        return redirect(url_for('estimate.adjust_estimate', id_control=id_control))
        
    
    query = Estimate.select(
        Nature.id.alias('id_nature'),
        Nature.name_nature,
        Estimate.id.alias('id_estimate'),
        Estimate.value_estimate).join(
            Nature, JOIN.RIGHT_OUTER, on=(
                (Estimate.id_nature == Nature.id) & 
                (Estimate.id_control == id_control))).where(
            Nature.id_user == current_user)
    natures = query.dicts()
    
    forms = []
    for nature in natures:
        form = EstimateForm()
        form.value_nature.label.text = nature['name_nature']
        form.value_nature.data = nature['value_estimate']
        form.id_estimate.data = nature['id_estimate']
        form.id_nature.data = nature['id_nature']
        forms.append(form)
    return render_template('estimate_natures.html', forms=forms, id_control=id_control)