from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, ValidationError
from database.models.user import User
from extensions import bcrypt

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    btn_submit = SubmitField('Login')
    
    def login(self):
        user = User.get_or_none(User.email_user == self.email.data)
        
        # Verifica se o email é cadastrado
        if user is None:
            raise ValidationError('Uer not found')

        # Verifica se a senha bate com a encriptada no banco
        if not bcrypt.check_password_hash(user.password_user, self.password.data):
            raise ValidationError('Invalid password')

        return user
            