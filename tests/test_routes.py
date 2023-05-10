from flask import Flask
import sys, json
sys.path.append("../flaskr")
from getquote import getquote_blueprint
from addquote import addquote_blueprint


def test_get_route():
    # defining app and registering the blueprint for GET route
    app = Flask(__name__)
    app.register_blueprint(getquote_blueprint)
    client = app.test_client()
    url = '/quote'

    # assigning response data to variable
    response = client.get(url)

    # testing if author and quote keys are in the response
    assert b"author" in response.get_data() and b"quote" in response.get_data()
    # testing if the response status code is 200
    assert response.status_code == 200

def test_post_route():
    # defining app and registering the blueprint for POST route
    app = Flask(__name__)
    app.register_blueprint(addquote_blueprint)

    client = app.test_client()

    url = '/addquote'

    # defining data to POST
    quoteData = {
        "author": "test",
        "quote": "test quote"
    }

    # sending the POST request
    response = client.post(url, data=json.dumps(quoteData), mimetype="application/json")
    # testing if the request was successful by checking if status code is 200
    assert response.status_code == 200