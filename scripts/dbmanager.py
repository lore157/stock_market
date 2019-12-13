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
    try:
        cursor.execute("SELECT * FROM register")
        '''# Print all elements of 'register' table, for control
        try_one = cursor.fetchall()
        for row in try_one:
            print("---------------------------------------")
            print("| ", row[0], " | ", row[1], " | ", row[2], " |")'''
    except sqlite3.OperationalError:
        # Create table
        cursor.execute('''CREATE TABLE register
                       (username TEXT, salt TEXT, digest TEXT,
                       PRIMARY KEY (username))''')
        print("Fixed blank database.\nNow you're able to register for full \
               access to our service.\nIf you want to do so, please use -a \
               USERNAME -p PASSWORD when running this program again.")
        print("Quitting the program now.")
        exit()
    return

def save_new_username(username, password, verbosity):
    global conn
    global cursor
    if verbosity:
        print("Registering user...")
    salt, digest = hash_password(password)
    cursor.execute('''INSERT OR REPLACE INTO register VALUES (?,?,?)''',
                   (username, salt, digest))
    conn.commit()
    print("\nUser successfully registered!")
    return

def hash_password(pw):
    salt = str(random.random())
    digest = salt+pw
    for i in range(1000000):
        digest = hashlib.sha256(digest.encode('utf-8')).hexdigest()
    return salt, digest

def check_for_username(username, password, verbosity):
    global conn
    global cursor
    try:
        temp = cursor.execute('''SELECT * FROM register
                              WHERE username=?''', (username,))
    except:
        temp = None

    if temp:
        temp2 = temp.fetchall()
        count = 0
        for row in temp2:
            if (count == 0):
                login_digest = row[1] + password
                count += 1
        if verbosity:
            print("\nRetrieving password...")
        for i in range(1000000):
            login_digest = hashlib.sha256(login_digest.encode('utf-8')).hexdigest()
    # Select DB row with relevant username
    try:
        rows = cursor.execute('''SELECT * from register
                              WHERE username=? AND digest=?''',
                              (username, login_digest))
        conn.commit()
        if verbosity:
            print("Done!")
    except:
        rows = None

    # Change program behaviour based on verified registration
    rows = rows.fetchall()
    
    if rows:
        registered = True
        print("\nUsername and password are correct.")
    else:
        registered = False
        print("\nUser is not present, or password is invalid.")
        if verbosity:
            print("If you want additional features, please register first \
or confirm username and password are written correctly.")

    return registered


   
