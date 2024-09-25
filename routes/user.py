from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user

user_route = Blueprint('user', __name__)

'''
    /user/register/              GET - Renderiza o form para registro de novos usuários
    /user/register/              POST - Envia dados do novo usuário registrado
    /user/<reference>/           GET - 
'''
    

@user_route.route('/register/', methods=['GET', 'POST'])
def register_user():
    from forms.user import UserForm
    form = UserForm()

    if form.validate_on_submit():
        user = form.save()
        login_user(user, remember=True)
        return redirect(url_for('moves.render_index'))
    elif 'email' in form.errors:
          return render_template('modal_warning.html')

    return render_template('form_register_user.html', form=form)