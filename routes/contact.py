from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user
from database.models.contact import Contact
from database.models.user import User

contact_route = Blueprint('contact', __name__)

'''
    - /contact/                 (GET) Renderizar um formulário para criar um contact
    - /contact/                 (POST) Insere um contact
    - /contact/all              (GET) Listar os contacts
    - /contact/<id>             (GET) Obter os dados de um contact   
    - /contact/<id>/edit        (GET) Renderizar um formulário para editar um contact
    - /contact/<id>/update      (PUT) Atualizar os dados de um contact
    - /contact/<id>/warning     (GET) Renderizar um formulário para editar um contact
    - /contact/<id>/delete      (DELETE) Deleta o registro do contact  
'''

@contact_route.route('/', methods=['GET', 'POST'])
def render_form():
    if not current_user.is_authenticated:
        return redirect(url_for('user.login'))
    from forms.contact import ContactForm
    form = ContactForm()
    
    if form.validate_on_submit():
        form.save()
        contacts = Contact.select().where(Contact.id_user == current_user)
        return render_template('contacts_list.html', contacts=contacts) 

    return render_template('form_contact.html', form=form)


@contact_route.route('/all', methods=['GET'])
def list_contacts():
    if not current_user.is_authenticated:
        return redirect(url_for('user.login'))
    
    contacts = Contact.select().where(Contact.id_user == current_user)
    return render_template('contacts_list.html', contacts=contacts)


@contact_route.route('/<int:id_contact>/edit')
def edit_contact(id_contact):
    if not current_user.is_authenticated:
        return redirect(url_for('user.login'))
    from forms.contact import ContactForm
    form = ContactForm()
    contact = Contact.get_by_id(id_contact)
    return render_template("form_contact.html", form=form, contact=contact)


@contact_route.route('/<int:id_contact>/update', methods=['PUT'])
def update_contact(id_contact):
    if not current_user.is_authenticated:
        return redirect(url_for('user.login'))
    from forms.contact import ContactForm
    form = ContactForm()
    
    if form.validate_on_submit():
        contacts = Contact.select().where(Contact.id_user == current_user)
        form.edit_save()
        return render_template('contacts_list.html', contacts=contacts)


@contact_route.route('/<int:id_contact>/warning')
def warning_contact(id_contact):
    if not current_user.is_authenticated:
        return redirect(url_for('user.login'))
    contact = Contact.get_by_id(id_contact)
    return render_template("contact_delete.html", contact=contact)


@contact_route.route('/<int:id_contact>/delete', methods=['DELETE'])
def delete_contact(id_contact):
    if not current_user.is_authenticated:
        return redirect(url_for('user.login'))
    
    contact_delete = Contact.delete().where(Contact.id_user == current_user).where(Contact.id == id_contact)
    contact_delete.execute()
    
    contacts = Contact.select().where(Contact.id_user == current_user)
    return render_template('contacts_list.html', contacts=contacts)