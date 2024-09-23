from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from database.models.user import User
from extensions import bcrypt

class UserForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmação da senha', validators=[DataRequired(), EqualTo('password')])
    btn_submit = SubmitField('Cadastrar')
    
    def validate_email(self, email):
        if User.get(User.email_user == email.data):
            return ValidationError('Email de usuário já cadastrado')
        
    def save(self):
        password = bcrypt.generate_password_hash(self.password.data.encode('utf-8'))
        
        user = User.create(
            name = self.name.data,
            email = self.email.data,
            password = password,
        )
        
        return user            