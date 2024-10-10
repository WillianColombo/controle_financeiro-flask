from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired
from database.models.contact import Contact
from flask_login import current_user

class ContactForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    description = StringField('Descrição')
    id = HiddenField()
    btn_submit = SubmitField('Cadastrar')

    def save(self):
        contact = Contact.create(
            name_contact = self.name.data,
            description_contact = self.description.data,
            id_user = current_user,
        )
        return contact
    
    def edit_save(self):
        contacts = (Contact.update(
            {
                Contact.name_contact: self.name.data, 
                Contact.description_contact: self.description.data
                }
            ).where(Contact.id_user == current_user).where(Contact.id == self.id.data))
        contacts.execute()
            