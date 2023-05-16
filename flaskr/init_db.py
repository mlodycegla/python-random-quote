import sqlite3, json

connection = sqlite3.connect("./instance/flaskr.sqlite")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS quotes (author, quote)")
cursor.execute("SELECT COUNT(*) FROM quotes")

if(cursor.fetchone()[0] == 0):
     quotesFile = json.load(open("./quotes.json"))
     columns = ["author", "quote"]
     for row in quotesFile["quotes"]:
            cursor.execute("INSERT INTO quotes (author, quote) values(" + f"'{row['author']}', '{row['quote']}')")

connection.commit()

def get_db_connection():
    connection = sqlite3.connect('./instance/flaskr.sqlite')
    return connection
