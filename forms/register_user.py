from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from database.models.user import User
from extensions import bcrypt
from peewee import DoesNotExist

class RegisterForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    confirm_password = PasswordField('Con. a senha', validators=[DataRequired(), EqualTo('password')])
    btn_submit = SubmitField('Cadastrar')
    
    def validate_email(self, email):
        try:
            user = User.get(User.email_user == email.data)
            raise ValidationError('Email de usuário já cadastrado')
        except DoesNotExist:
            pass
        
    def save(self):
        password = bcrypt.generate_password_hash(self.password.data.encode('utf-8'))
        
        user = User.create(
            name_user = self.name.data,
            email_user = self.email.data,
            password_user = password,
        )
        
        return user            