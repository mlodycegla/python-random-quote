from flask import Blueprint, request
import json

# opening the quotes file, assigning it to a variable for later use
with open('quotes.json', "r", encoding='utf-8') as quotesFileForRead:
  quotesObject = json.load(quotesFileForRead)

status_codes = {400: "400 Bad request", 200: "Ok"}

# defining the POST route for adding new user created quotes to the database
addquote_blueprint = Blueprint("addquote", __name__)
@addquote_blueprint.route('/addquote', methods=['POST'])
def addquote():
    # assigning user input to variable
    requestjson = request.get_json()
    # checking if user input is empty
    if requestjson == {}:
        return status_codes[400], 400
    # checking if user input has quote key and author key
    if "quote" not in requestjson or "author" not in requestjson:
        return status_codes[400], 400
    # checking if the values for keys are empty
    if requestjson["quote"] == "" or requestjson["author"] == "":
        return status_codes[400], 400
    
    # initialazing newquote variable
    newquote = {}
    # assigning user input to the variable
    newquote["quote"] = requestjson["quote"]
    newquote["author"] = requestjson["author"]
    # appending the new quote to json object from quotes file
    quotesObject["quotes"].append(newquote)
    # trying to add the new quote to the quotes file
    try:
        # opening quotes file for writing new quotes to it
        quotesFileForWrite = open('quotes.json', "w", encoding='utf-8')
        json.dump(quotesObject, quotesFileForWrite)
        return status_codes[200]
    except Exception as error:
        return status_codes[400], + f": {error}", 400