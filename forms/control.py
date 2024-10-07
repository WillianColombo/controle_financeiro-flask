from flask_wtf import FlaskForm
from wtforms import MonthField, SubmitField
from wtforms.validators import DataRequired
from database.models.control import Control
from flask_login import current_user

class ControlForm(FlaskForm):
    month_year = MonthField(validators=[DataRequired()])
    btn_submit = SubmitField('Cadastrar')

    def save(self):
        control = Control.create(
            month_control = self.month_year.data.month,
            year_control = self.month_year.data.year,
            month_year_control = self.month_year.data,
            id_user = current_user,
        )
        
        return control
            