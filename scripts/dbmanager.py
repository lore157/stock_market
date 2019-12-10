import sqlite3
import hashlib
import argparse


conn = None
cursor = None

def open_and_create():
    global conn
    global cursor
    conn = sqlite3.connect('credentials.db')
    cursor = conn.cursor()
    print("OK 1.1!")
    try:
        cursor.execute("SELECT * FROM register")
        print("OK 1.2!")
    except sqlite3.OperationalError:
        # Create tables
        cursor.execute('''CREATE TABLE register
                       (username TEXT, salt TEXT,
                       PRIMARY KEY (username))''')
        print("OK 1.3!")
        cursor.execute('''CREATE TABLE login
                       (username TEXT, digest TEXT,
                       PRIMARY KEY (username),
                       FOREIGN KEY (username) REFERENCES register(username))''')
        print("OK 1.4!")
    return

def save_new_username(username, password):
    global conn
    global cursor
    digest = hashlib.sha256(password.encode('utf-8')).hexdigest()
    cursor.execute("INSERT OR REPLACE INTO name VALUES (?,?)",
                   (username, digest))
    cursor.execute("INSERT OR REPLACE INTO value VALUES (?,?)",
                   (username, 10))
    conn.commit()
    return



