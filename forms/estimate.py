from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError
from database.models.estimate import Estimate
from database.models.nature import Nature
from database.models.user import User
from flask_login import current_user
from peewee import DoesNotExist

class EstimateForm(FlaskForm):
    choices = (Nature.select(Nature, User))
    
    name = StringField('Estimativa', validators=[DataRequired()])
    natures = SelectField(choices=[()] ,validators=[DataRequired()])
    btn_submit = SubmitField('Cadastrar')
    
    def validate_name(self, name):
        try:
            nature = Estimate.get(Estimate.name_nature == name.data)
            raise ValidationError('nature already registered')
        except DoesNotExist:
            pass

    def save(self):
        nature = Estimate.create(
            name_nature = self.name.data,
            description_nature = self.description.data,
            id_user = current_user,
        )
        return nature
            