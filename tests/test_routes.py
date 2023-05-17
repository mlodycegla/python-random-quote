from flask import Flask
import sys, json
sys.path.append("../flaskr")
from getquote import getquote_blueprint
from addquote import addquote_blueprint
from init_db import get_db_connection


def test_get_route():
    # defining app and registering the blueprint for GET route
    app = Flask(__name__)
    app.register_blueprint(getquote_blueprint)
    client = app.test_client()
    url = '/quote'

    # getting the response from API
    response = client.get(url)

    assert b"author" in response.get_data() and b"quote" in response.get_data()
    assert response.status_code == 200

def test_post_route():
    # defining app and registering the blueprint for POST route
    app = Flask(__name__)
    app.register_blueprint(addquote_blueprint)

    client = app.test_client()

    url = '/addquote'

    # mock data for POST request
    quoteData = {
        "author": "test",
        "quote": "test quote"
    }

    response = client.post(url, data=json.dumps(quoteData), mimetype="application/json")
    assert response.status_code == 200

def test_db_connection():
    connection = get_db_connection()
    cursor = connection.cursor()
    # testing if select and insert works with mock data
    cursor.execute("SELECT * FROM quotes")
    cursor.execute("INSERT INTO quotes (author, quote) VALUES ('test', 'quote')")