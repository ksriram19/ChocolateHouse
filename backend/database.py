import sqlite3

def get_database_connection():
    return sqlite3.connect("chochouse.db")
