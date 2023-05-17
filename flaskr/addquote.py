from flask import Blueprint, request
from init_db import get_db_connection

status_codes = {500: ("<b>500 Internal server error<b>", 500), 400: ("<b>400 Bad request</b>", 400), 200: ("<b>Ok</b>", 200)}

# defining the POST route for adding new user created quotes to the database
addquote_blueprint = Blueprint("addquote", __name__)
@addquote_blueprint.route('/addquote', methods=['POST'])
def addquote():
    connection = get_db_connection()
    cursor = connection.cursor()
    userInputJson = request.get_json()

    # checking if user input is correct
    if(not len(userInputJson["author"]) or not len(userInputJson["quote"])):
        return status_codes[400]

    # collecting user input for later adding into database
    newquote = {}
    newquote["quote"] = userInputJson["quote"]
    newquote["author"] = userInputJson["author"]
    # trying to add the new quote to the database
    try:
        cursor.execute(f"INSERT INTO quotes (author, quote) VALUES ('{newquote['author']}', '{newquote['quote']}')")
        connection.commit()
        return status_codes[200]
    except Exception as error:
        return f"{error} ", status_codes[500]