from flask import Flask
app = Flask(__name__)
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///Employees.db'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

app.run(host='localhost', port=5000)

