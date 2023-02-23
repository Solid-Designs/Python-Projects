from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__, template_folder='template')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", text='Testing')

@auth.route('/logout')
def logout():
    return "<p>logout</p"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
    
        if len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(firstName) < 1:
            flash('First name must be greater than 0 characters', category='error')
        elif password1 != password2:
            flash('Passwords dont match', category='error')
        elif len(password1) < 7:
            flash('Password must be more than 7 characters', category='error')
        else:
            flash('Account created!', category='success')


    return render_template("sign_up.html")