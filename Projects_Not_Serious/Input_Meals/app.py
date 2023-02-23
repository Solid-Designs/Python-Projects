from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def submit_meal():
    return render_template('index.html')

@app.route('/display', methods = ['GET', 'POST'])
def display_meals():
    if request.method == 'POST':
        result = request.form
        for key, values in result.items():
            print(key)
            print(values)
        return render_template('display.html')

if __name__ == '__main__':
    app.run(debug=True)