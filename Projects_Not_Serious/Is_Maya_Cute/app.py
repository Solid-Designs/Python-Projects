from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cute', methods = ['POST', 'GET'])
def confirm_cute():
    if request.method == 'POST':
        result = request.form
        result_list = list(result.items())[0]
        return render_template('cute.html', result = result_list)
    

if __name__ == '__main__':
    app.run()