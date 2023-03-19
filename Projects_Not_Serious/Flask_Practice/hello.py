from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = 'Burrito'
    list_of_meals = ['Chicken nuggets', 'Tacos', 'Lo Mein']
    return render_template('index.html', title='Yo', username=name, meals=list_of_meals)

@app.route('/chicken/<name>')
def chicken(name):
    return 'Chicken', 'name'

@app.route('/login')
def login():
    if request.method == "POST":
        user = request.form["name"]
    return render_template('login.html')

@app.route('dashboard/<name>')
def dashboard(name):
    return 'Welcome %s' % name

if __name__ == '__main__':
    app.run(debug=True)