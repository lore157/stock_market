import sqlite3
import hashlib
import random

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
        # Printing all elements of 'register' table, for control
        try_one = cursor.fetchall()
        for row in try_one:
            print("| ", row[0], " | ", row[1], " |")
            print("---------------------------------------")
        print("OK 1.3!")
        '''# Printing all elements of 'login' table, for control
        cursor.execute("SELECT * FROM login")
        try_two = cursor.fetchall()
        for row in try_two:
            print("| ", row[0], " | ", row[1], " |")
            print("---------------------------------------")
        print("OK 1.4!")'''
    except sqlite3.OperationalError:
        # Create tables
        cursor.execute('''CREATE TABLE register
                       (username TEXT, salt TEXT,
                       PRIMARY KEY (username))''')
        print("OK 1.5!")
        cursor.execute('''CREATE TABLE login
                       (username TEXT, digest TEXT,
                       PRIMARY KEY (username),
                       FOREIGN KEY (username) REFERENCES register(username))''')
    return

def save_new_username(username, password):
    global conn
    global cursor
    salt, digest = hash_password(password)
    cursor.execute('''INSERT OR REPLACE INTO register VALUES (?,?)''',
                   (username, salt))
    cursor.execute('''INSERT OR REPLACE INTO login VALUES (?,?)''',
                   (username, digest))
    conn.commit()
    return

def hash_password(pw):
    salt = str(random.random())
    digest = salt+pw
    for i in range(1000000):
        digest = hashlib.sha256(digest.encode('utf-8')).hexdigest()
    return salt, digest

def check_for_username(username, password):
    global conn
    global cursor
    temp = cursor.execute('''SELECT salt FROM register
                          WHERE username=?''', (username))
    print('PROVA 3')
    if temp:
        login_digest = temp + password
        for i in range(1000000):
            login_digest = hashlib.sha256(digest.encode('utf-8')).hexdigest()
    # DB with all registered users
    print('PROVA 4')
    rows = cursor.execute('''SELECT * from register JOIN login
      WHERE register.username = login.username''')
    print("ROWS: ", rows)
    result = cursor.execute('''SELECT * FROM rows
                   WHERE username=? AND digest=?''', (username, login_digest))
    conn.commit()
    person = cursor.fetchall()
    print("PERSON: ", person)
    # NOTE: this could be done more efficiently with a JOIN
    if person:
        pass
    else:
        print("User is not present, or password is invalid")


   
