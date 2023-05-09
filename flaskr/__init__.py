from flask import Flask
# importing the blueprints from seperate files
from getquote import getquote_blueprint
from addquote import addquote_blueprint

app = Flask(__name__)
app.register_blueprint(getquote_blueprint)
app.register_blueprint(addquote_blueprint)

if __name__ == '__main__':
    app.run()