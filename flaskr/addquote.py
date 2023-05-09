from flask import Blueprint, request
import json

# opening the quotes file and assigning it to a variable for later use
with open('quotes.json', "r", encoding='utf-8') as quotesFileForRead:
  quotesObject = json.load(quotesFileForRead)

status_codes = {500: "500 Internal server error", 400: "400 Bad request", 200: "Ok"}

# defining the POST route for adding new user created quotes to the database
addquote_blueprint = Blueprint("addquote", __name__)
@addquote_blueprint.route('/addquote', methods=['POST'])
def addquote():
    # assigning user input to variable
    userInputJson = request.get_json()
    # checking if user input is empty
    if userInputJson == {}:
        return status_codes[400], 400
    # checking if user input has quote key and author key
    if "quote" not in userInputJson or "author" not in userInputJson:
        return status_codes[400], 400
    # checking if the values for keys are empty
    if userInputJson["quote"] == "" or userInputJson["author"] == "":
        return status_codes[400], 400
    
    # initialazing newquote variable
    newquote = {}
    # assigning user input to the variable
    newquote["quote"] = userInputJson["quote"]
    newquote["author"] = userInputJson["author"]
    # appending the new quote to json object from quotes file
    quotesObject["quotes"].append(newquote)
    # trying to add the new quote to the quotes file
    try:
        # opening quotes file for writing new quotes to it
        quotesFileForWrite = open('quotes.json', "w", encoding='utf-8')
        # adding new quote to the file and returning code 200 if successful
        json.dump(quotesObject, quotesFileForWrite)
        return status_codes[200]
    except Exception as error:
        # if this failed returns code 500 for internal server error and the exception
        return status_codes[500], + f": {error}", 500