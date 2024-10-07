from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from wtforms.validators import ValidationError

user_route = Blueprint('user', __name__)

'''
    /user/register/              GET - Renderiza o form para registro de novos usuários
    /user/register/              POST - Envia dados do novo usuário registrado
    /user/login/                 GET - Renderiza o form para login de usuário
    /user/login/                 POST - Envia dados da tentativa de login do usuário
    /user/logout/                GET - Faz o logout do usuário logado
'''
    

@user_route.route('/register', methods=['GET', 'POST'])
def register_user():
    from forms.register_user import RegisterForm
    form = RegisterForm()

    
    if form.validate_on_submit():
        user = form.save()
        login_user(user, remember=True)
        return redirect(url_for('home.render_home'))
    elif 'email' in form.errors and 'Email de usuário já cadastrado' in form.errors['email']:
        flash('Email de usuário já cadastrado!')
        return redirect(url_for('user.register_user'))
    elif 'confirm_password' in form.errors and 'Field must be equal to password.' in form.errors['confirm_password']:
        flash('As senhas não são iguais!')
        return redirect(url_for('user.register_user'))
    elif 'password' in form.errors and 'Invalid input.' in form.errors['password']:
        flash('''
A senha deve conter:
- Pelo menos 10 caracteres
- Pelo menos 1 letra maiúscula
- Pelo menos 1 letra minúscula
- Pelo menos 1 número''')
        return redirect(url_for('user.register_user'))

    return render_template('form_register_user.html', form=form)

@user_route.route('/login', methods=['GET', 'POST'])
def login():
    from forms.login_user import LoginForm
    form = LoginForm()

    try:
        if form.validate_on_submit():
            user = form.login()
            login_user(user, remember=True)
            return redirect(url_for('home.render_home'))
    except ValidationError:
        flash('Usuário ou senha incorreta!')
        return redirect(url_for('user.login'))

    return render_template('form_login_user.html', form=form)

@user_route.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('user.login'))