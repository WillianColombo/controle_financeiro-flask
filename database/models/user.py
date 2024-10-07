from peewee import Model, CharField
from database.database import db
from flask_login import UserMixin
from extensions import login_manager

@login_manager.user_loader
def load_user(user_id):
    try:
        return User.get(User.id == user_id)
    except:
        pass

class User(Model, UserMixin):
    name_user = CharField(max_length=80)                                    # Varchar
    email_user = CharField()                                                # Varchar
    password_user = CharField()                                           # Varchar

    class Meta:
        database = db # Indica que o modelo será tabela do 'felideos.db'