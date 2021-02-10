import os
from flask import Flask, g
from flask_cors import CORS
from .extensions import db
from .routes.users import users
from .routes.products import products

def create_app(test_config=None):
    #create and configure the app
    
    app = Flask(__name__, instance_relative_config=True)
    #app.config.from_mapping(
    #    FLASK_ENV ='development',
    #    DEBUG = True
    #)
    app.config.from_pyfile('config.py', silent=False)
    

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    CORS(app)

    with app.app_context():
        app.register_blueprint(users)
        app.register_blueprint(products)

        return app

