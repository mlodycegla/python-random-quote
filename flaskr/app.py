import os
from flask import Flask
from getquote import getquote_blueprint
from addquote import addquote_blueprint

def create_app():
    app = Flask(__name__)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(getquote_blueprint)
    app.register_blueprint(addquote_blueprint)

    return app

if __name__ == '__main__':
    create_app()