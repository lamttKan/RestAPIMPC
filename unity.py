import sqlite3
from sqlite3.dbapi2 import Cursor

def questions(query):
    conn = sqlite3.connect("IntroFlask/dbquestion.db")
    curson =  conn.execute(query).fetchall()
    conn.close()
    return curson

if __name__ == "__main__":
    print(questions("SELECT * FROM questions"))