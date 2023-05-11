from flask import Blueprint
import random, json, os

with open(os.path.abspath("../flaskr/quotes.json"), "r", encoding='utf-8') as quotesFile:
  quotesObject = json.load(quotesFile)

# defining the GET route which returns a random quote and it's author
getquote_blueprint = Blueprint("getquote", __name__)
@getquote_blueprint.route('/quote', methods=['GET'])
def quote():
    # getting a random quote and returning
    quotesLength = len(quotesObject["quotes"])
    quotesRange = random.randint(0, quotesLength - 1)
    return quotesObject['quotes'][quotesRange], 200