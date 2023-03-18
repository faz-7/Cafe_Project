
from Cafe_Project.core.db_manager import session
from Cafe_Project.models.table import Table
from core.db_manager import session
from models.table import Table


def add_table(position, available):
    table = Table(position=position, available=available)
    session.add(table)
    session.commit()


def check_table():
    table = session.query(Table).filter_by(available=True).first()
    return table.id


def reserve(table_id):
    table = session.query(Table).filter_by(id=table_id).first()
    table.available = False
    session.commit()
    
def assign_table():
    table = session.query(Table).filter_by(available=True).first()
    if table:
        return table.id

