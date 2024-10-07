from peewee import Model, DecimalField, ForeignKeyField
from database.models.nature import Nature
from database.models.control import Control
from database.database import db

class Estimate(Model):
    value_estimate = DecimalField(decimal_places=2)
    id_control = ForeignKeyField(Control)
    id_nature = ForeignKeyField(Nature)

    class Meta:
        database = db # Indica que o modelo será tabela do 'felideos.db'