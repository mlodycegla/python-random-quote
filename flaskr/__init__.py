# quotes from https://gist.github.com/nasrulhazim/54b659e43b1035215cd0ba1d4577ee80
from flask import Flask
from getquote import getquote_blueprint
from addquote import addquote_blueprint

app = Flask(__name__)
app.register_blueprint(getquote_blueprint)
app.register_blueprint(addquote_blueprint)

if __name__ == '__main__':
    app.run()