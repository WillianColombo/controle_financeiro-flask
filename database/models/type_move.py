from peewee import Model, CharField
from database.database import db

class TypeMove(Model):
    name_type = CharField(max_length=30) 

    class Meta:
        database = db # Indica que o modelo será tabela do 'felideos.db'