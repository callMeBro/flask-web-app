# This file makes the webite folder a python package

# import flask 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()               #add something to bd..
DB_NAME = "my_db.db"

def create_app():
    app = Flask(__name__)               # __name__ represents the name of the file 
    app.config['SECRET_KEY'] = 'HBJBFSJKDNKJFD DKLFJKFDNSFD'                #set up config varible['S'] that encryps the cookies and session data relating to our website 
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'                 # store db as DBNAME in website directory  
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'                 # store db as DBNAME in website directory  
    
    # db_url
    db.init_app(app)

    
    #tell flask that we have blueprints containing different views for our app
    from .views import views
    from .auth import auth
    # register blueprint with flack application 
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # define models class befor database creation
    from .models import User, Note

    create_database(app)

    # The login manager contains the code that lets your application and Flask-Login work together
    login_manager = LoginManager()
    login_manager.login_message = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return app

def create_database(app):
    # Use the application context
    with app.app_context():
        # if not path.exists('website/mydatabase.db'):
        if not path.exists('website/'+DB_NAME):

            db.create_all()
            print('Created Database')
        else:
            print('Database already exists.')


            

