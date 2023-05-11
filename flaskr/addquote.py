from flask import Blueprint, request
import json, os

with open(os.path.abspath("../flaskr/quotes.json"), "r", encoding='utf-8') as quotesFileForRead:
  quotesObject = json.load(quotesFileForRead)

status_codes = {500: ("500 Internal server error", 500), 400: ("400 Bad request", 400), 200: ("Ok", 200)}

# defining the POST route for adding new user created quotes to the database
addquote_blueprint = Blueprint("addquote", __name__)
@addquote_blueprint.route('/addquote', methods=['POST'])
def addquote():
    userInputJson = request.get_json()

    # checking if user input is correct
    if not userInputJson or not all(key in userInputJson for key in ["quote", "author"]) or any(not userInputJson[key] for key in ["quote", "author"]):
        return status_codes[400]
    
    # collecting user input for later adding into file
    newquote = {}
    newquote["quote"] = userInputJson["quote"]
    newquote["author"] = userInputJson["author"]
    quotesObject["quotes"].append(newquote)
    # trying to add the new quote to the quotes file
    try:
        quotesFileForWrite = open('quotes.json', "w", encoding='utf-8')
        json.dump(quotesObject, quotesFileForWrite)
        return status_codes[200]
    except Exception as error:
        return f"{error} ", status_codes[500]