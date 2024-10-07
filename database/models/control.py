from peewee import Model, IntegerField, ForeignKeyField, DateField
from database.models.user import User
from database.database import db

class Control(Model):
    month_control = IntegerField() 
    year_control = IntegerField()
    month_year_control = DateField()
    id_user = ForeignKeyField(User)

    class Meta:
        database = db # Indica que o modelo será tabela do 'felideos.db'