import sqlalchemy

from Cafe_Project.core.db_manager import session
from Cafe_Project.models.receipts import Receipt


def get_id():
    id = session.query(Receipt).order_by(sqlalchemy.desc(Receipt.id)).first()
    return id + 1
