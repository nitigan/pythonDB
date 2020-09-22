from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datatables import ColumnDT, DataTables
import datetime
import random
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///sites.db'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    phone = db.Column(db.String(10))
    birthday = db.Column(db.Date)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/load_table_sql',methods =['GET','POST'])
def load_table_sql():
    columns = [
        ColumnDT(User.id),
        ColumnDT(User.name),
        ColumnDT(User.phone),
        ColumnDT(User.birthday),
    ]
    query = db.session.query().select_from(User)
    rowTable = DataTables(request.args.to_dict(),query,columns)

    # returns what is needed by DataTable
    return rowTable.output_result()

def random_date():
    start_date = datetime.date(1997,1 ,1)
    end_data = datetime.date(2010, 1, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_dats = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    return random_date

def create_db_user():
    db.create_all()
    for i in range(10):
        user = User(name='user'+str(i),phone='phone'+
                    str(i),birthday=random_date())
        db.session.add(user)
    db.session.commit()
    print('create done')
    show_db_user()

if __name__ = "__main__":
    app.run(host='0.0.0.0',debug=True)
    