from flask import Flask, render_template, url_for, request, redirect

from models.user import User
from models.table import Table
from models.receipts import Receipt
from Cafe_Project.menu_items.utils import MenuItems, get_item
from Cafe_Project.table.utils import assign_table
from Cafe_Project.receipt.utils import get_id
from Cafe_Project.user.utils import create_receipt

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html', title='about')


@app.route('/signup')
def signup_page():
    return render_template('signup.html')


@app.route('/sign_up', methods=['POST'])
def sign_up():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    phone = request.form['phone']
    password = request.form['password']
    User.add(4, first_name, last_name, phone, email, password)
    return render_template('index.html')


@app.route('/login')
def login_page():
    # return render_template('receipt.html')
    return render_template('login.html')
    # items = list(get_item())
    # return render_template('menu_item.html', items=items)


@app.route('/menu_item')
def menu_item():
    items = list(get_item())
    return render_template('menu_item.html', items=items)


@app.route('/receipt')
def receipt():
    pass


# @app.route('/create_receipt/<integer:id>', methods=['GET', 'POST'])
# def create_receipt(id):
#     if assign_table():
#         Receipt.add(id=id, user_id=id, table_id=assign_table(), total_price=0, pay=False)
#     else:
#         pass


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            if User.check_login(request.form['username'], request.form['password']):
                create_receipt(request.form['password'])
                return redirect(url_for('home'))
            else:
                error = "<h1> invalid user pass </h1>"
                return render_template('login.html', error=error)
                # todo: error

        else:
            # todo: cashier panel
            error = 'Invalid Credentials. Please try again.'

    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
