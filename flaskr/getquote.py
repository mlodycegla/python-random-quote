from flask import Blueprint
from init_db import get_db_connection

# defining the GET route which returns a random quote and it's author
getquote_blueprint = Blueprint("getquote", __name__)
@getquote_blueprint.route('/quote', methods=['GET'])
def quote():
    # getting a random quote from database and returning
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM quotes ORDER BY RANDOM() LIMIT 1")
    quote = cursor.fetchone()
    formattedQuote = {"author": quote[0], "quote": quote[1]}
    return formattedQuote, 200