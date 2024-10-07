from peewee import Model, CharField, ForeignKeyField
from database.models.user import User
from database.database import db

class Contact(Model):
    name_contact = CharField() 
    description_contact = CharField(null = False)  
    id_user = ForeignKeyField(User)

    class Meta:
        database = db # Indica que o modelo será tabela do 'felideos.db'