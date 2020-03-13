from flask import Flask
from . import views

def create_app(test_config=None):
    app = Flask(__name__)

    app.register_blueprint(views.bp)

   

    return app
