from flask import Flask

# Creates the app and returns itself with all the functions available in flask
# Since it is an __init__.py file, this makes it a module, and any function created here can be imported
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ajidofahpecaefa gpoeiafj'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
