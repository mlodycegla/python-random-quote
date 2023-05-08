# importing app and a variable containing the quotes from the main file
from flask import Blueprint
import random, json

# opening the quotes file and assigning it to a variable for later use
with open('quotes.json', "r", encoding='utf-8') as quotesFile:
  quotesObject = json.load(quotesFile)

# defining the GET route which returns a random quote and it's author
getquote_blueprint = Blueprint("getquote", __name__)
@getquote_blueprint.route('/quote', methods=['GET'])
def quote():
    quotesLength = len(quotesObject["quotes"])
    quotesRange = random.randint(0, quotesLength - 1)
    return quotesObject['quotes'][quotesRange], 200