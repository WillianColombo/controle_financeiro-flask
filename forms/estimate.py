from flask_wtf import FlaskForm
from wtforms import DecimalField, HiddenField, SubmitField
from wtforms.validators import DataRequired
from database.models.estimate import Estimate
from flask_login import current_user

class EstimateForm(FlaskForm):
    id_estimate = HiddenField()
    id_nature = HiddenField()
    value_nature = DecimalField(validators=[DataRequired()])    
    
    def save(self, id_control, id_nature):
        estimate = Estimate.create(value_estimate=self.value_nature.data, id_control=id_control, id_nature=id_nature)
    
    def edit_save(self):
        estimates = (Estimate.update(
            {Estimate.value_estimate: self.value_nature.data}).where(
                Estimate.id == self.id_estimate.data)).execute()
        return estimates