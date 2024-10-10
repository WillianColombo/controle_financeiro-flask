from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired, ValidationError
from database.models.nature import Nature
from flask_login import current_user
from peewee import DoesNotExist

class NatureForm(FlaskForm):
    name = StringField('Natureza', validators=[DataRequired()])
    description = StringField('Descrição')
    id = HiddenField()
    btn_submit = SubmitField('Cadastrar')
    
    def validate_name(self, name):
        try:
            nature = Nature.get(Nature.name_nature == name.data)
            raise ValidationError('nature already registered')
        except DoesNotExist:
            pass

    def save(self):
        nature = Nature.create(
            name_nature = self.name.data,
            description_nature = self.description.data,
            id_user = current_user,
        )
        return nature
    
    def edit_save(self):
        natures = (Nature.update(
            {
                Nature.name_nature: self.name.data, 
                Nature.description_nature: self.description.data
                }
            ).where(Nature.id_user == current_user).where(Nature.id == self.id.data))
        natures.execute()
            