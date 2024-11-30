import sqlite3
def get_connection(db_name="example.db"):
    return sqlite3.connect(db_name)