from database.models.type_move import TypeMove
from peewee import DoesNotExist

def seeding():
    inserts = [
        {'name_type': 'fatura'},
        {'name_type': 'saida'},
        {'name_type': 'entrada'},
    ]
    for insert in inserts:
        try:
            result = TypeMove.get(TypeMove.name_type == insert['name_type'])
        except DoesNotExist:
            TypeMove.insert(name_type=insert['name_type']).execute()

seeding()
            