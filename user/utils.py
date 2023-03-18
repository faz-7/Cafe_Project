from Cafe_Project.core.db_manager import session
from Cafe_Project.models.user import User
from Cafe_Project.models.receipts import Receipt
from Cafe_Project.table.utils import assign_table
from models.user import User
from core.db_manager import session


def create_receipt(password):
    user_id = session.query(User).filter_by(password=password).first().id
    if assign_table():
        Receipt.add(id=user_id, user_id=user_id, table_id=assign_table(), total_price=0, pay=False)
    else:
        pass
        # todo: check this for first add to cart

def add_user(username, fname, lname, phone, email, password):
    user = User(username=username, fname=fname, lname=lname, phone=phone, email=email, password=password)
    session.add(user)
    session.commit()


def check_login(username, password):
    # question = session.query(User).filter_by(id=1).all()
    users = session.query(User).all()
    for q in users:
        if str(q.username) == username:
            if str(q.password) == password:
                return True


def check_username(username):
    users = session.query(User).all()
    for q in users:
        if str(q.username) == username:
            return False
    return True


def get_id(username):
    user_id = session.query(User).filter_by(username=username).first().id
    return user_id

