import sqlite3, json, os

# connecting to database and checking if the table is empty
connection = sqlite3.connect(os.path.abspath("../flaskr/instance/flaskr.sqlite"))
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS quotes (author, quote)")
cursor.execute("SELECT COUNT(*) FROM quotes")

# populating the table if it was empty
if(cursor.fetchone()[0] == 0):
     quotesFile = json.load(open("./quotes.json"))
     columns = ["author", "quote"]
     for row in quotesFile["quotes"]:
            cursor.execute("INSERT INTO quotes (author, quote) values(" + f"'{row['author']}', '{row['quote']}')")

connection.commit()

def get_db_connection():
    connection = sqlite3.connect(os.path.abspath("../flaskr/instance/flaskr.sqlite"))
    return connection
