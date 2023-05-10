from flask import Blueprint
import random, json, os

# opening the quotes file and assigning it to a variable for later use
with open(os.path.abspath("../flaskr/quotes.json"), "r", encoding='utf-8') as quotesFile:
  quotesObject = json.load(quotesFile)

# defining the GET route which returns a random quote and it's author
getquote_blueprint = Blueprint("getquote", __name__)
@getquote_blueprint.route('/quote', methods=['GET'])
def quote():
    # defining the lenght of quotes array which is located in the file 
    quotesLength = len(quotesObject["quotes"])
    # getting a random quote within the range of the array and returning it
    quotesRange = random.randint(0, quotesLength - 1)
    return quotesObject['quotes'][quotesRange], 200