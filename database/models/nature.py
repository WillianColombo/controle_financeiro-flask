from peewee import Model, CharField, ForeignKeyField
from database.models.user import User
from database.database import db

class Nature(Model):
    name_nature = CharField(max_length=50) 
    description_nature = CharField(null = False)  
    id_user = ForeignKeyField(User)

    class Meta:
        database = db # Indica que o modelo será tabela do 'felideos.db'