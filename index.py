# quotes from https://gist.github.com/nasrulhazim/54b659e43b1035215cd0ba1d4577ee80
from flask import Flask
from flask import request
from flask_restful import Api
import random
import json


with open('data.json', "r", encoding='utf-8') as f:
  data = json.load(f)

app = Flask(__name__)
api = Api(app)

@app.route('/quote', methods=['GET'])
def quote():
    return data['quotes'][random.randint(0, len(data['quotes']) - 1)], 200

@app.route('/addquote', methods=['POST'])
def addquote():
    if "quote" in request.get_json() and "author" in request.get_json():
        newquote = {"quote": 0, "author": 0}
        newquote["author"] = request.get_json()["author"]
        newquote["quote"] = request.get_json()["quote"]
        data["quotes"].append(newquote)
        with open('data.json', "w", encoding='utf-8') as f:
            try:
                json.dump(data, f)
                return "200 OK", 200
            except Exception as e:
                return "400 Bad request: " + e, 400
    return "406 Not Acceptable", 406

if __name__ == '__main__':
    app.run()