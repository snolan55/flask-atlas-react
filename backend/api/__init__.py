from flask import Flask, g
from flask_mongoengine import MongoEngine
from instance.config import *

db = MongoEngine()

def create_app(test_config=None):
    #create and configure the app
    
    app = Flask(__name__, instance_relative_config=True)
    
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=False)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    with app.app_context():
        app.register_blueprint(routes_bp)

        return app