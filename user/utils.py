from Cafe_Project.core.db_manager import session
from Cafe_Project.models.user import User
from Cafe_Project.models.receipts import Receipt
from Cafe_Project.table.utils import assign_table


def create_receipt(password):
    user_id = session.query(User).filter_by(password=password).first().id
    if assign_table():
        Receipt.add(id=user_id, user_id=user_id, table_id=assign_table(), total_price=0, pay=False)
    else:
        pass
        # todo: check this for first add to cart
