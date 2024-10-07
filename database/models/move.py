from peewee import Model, DecimalField, ForeignKeyField, CharField, DateTimeField, IntegerField
from database.models.nature import Nature
from database.models.control import Control
from database.models.user import User
from database.models.contact import Contact
from database.models.type_move import TypeMove
from database.database import db
import datetime

class Move(Model):
    value_move = DecimalField(decimal_places=2)
    description_move = CharField(null = False)
    current_installment_move = IntegerField()
    total_intallment_move = IntegerField()
    date_move = DateTimeField(default=datetime.datetime.now)
    
    id_control = ForeignKeyField(Control)
    id_nature = ForeignKeyField(Nature)
    id_type = ForeignKeyField(TypeMove)
    id_user = ForeignKeyField(User)
    id_contact = ForeignKeyField(Contact)

    class Meta:
        database = db # Indica que o modelo será tabela do 'felideos.db'