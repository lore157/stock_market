import sqlite3
import hashlib
import random


conn = None
cursor = None


def open_and_create():
    """Create and populate the table containing the users and the password

    This function creates the local database and selects all the entries of
    the table; if it doesn't find the table the program creates a new one."""

    global conn
    global cursor
    conn = sqlite3.connect('credentials.db')
    cursor = conn.cursor()
    try:
        # Extracting data from the database
        cursor.execute("SELECT * FROM register")
    except sqlite3.OperationalError:
        # Table creation
        cursor.execute('''CREATE TABLE register
                       (username TEXT, salt TEXT, digest TEXT,
                       PRIMARY KEY (username))''')
        print("Fixed blank database.\nNow you're able to register for full \
access to our service.\nIf you want to do so, please use -a \
USERNAME -p PASSWORD when running this program again.")
        sys.exit()
    return


def save_new_username(username, password, verbosity):
    """Registering users when they are logging-in for the first time

    Defining salt and digest of each user and saving it in the table.

    :param username: the username provided by the user for the authentication
    :param password: the password provided by the user for the authentication
    :param verbosity: the level of verbosity when directly required by the user
    :return: confirm that the registration process was succesfully concluded
    """


    global conn
    global cursor
    if verbosity:
        print("Registering user...")
    salt, digest = hash_password(password)  # Encrypting the password
    cursor.execute('''INSERT OR REPLACE INTO register VALUES (?,?,?)''',
                   (username, salt, digest))
    conn.commit()

    print("\nUser successfully registered!")
    return


def hash_password(pw):
    """Encrypt the password

    The program will compute the digest with a random salt and than perform
    the hashing process.


    :param pw: the local variable containing the password
    :return: salt and digest of the user's password
    :r_type:str, str
    """

    salt = str(random.random())
    digest = salt+pw
    # Repeating the hash 1000000 to increase security
    for i in range(1000000):
        digest = hashlib.sha256(digest.encode('utf-8')).hexdigest()
    return salt, digest


def check_for_username(username, password, verbosity):
    """Check if the username is registered in the DB

    The function looks for the rows containing the username that
    is trying to log-in. If no row is found the user is new or the input
    had a typo so the program will work in demo mode.


    :param username: the username provided by the user for the authentication
    :param password: the password provided by the user for the authentication
    :param verbosity: the lavel of verbosity when directly required by the user
    :return: True If the user is already registered, otherwise False.
    :rtype: Boolean
    """

    global conn
    global cursor
    try:
        temp = cursor.execute('''SELECT * FROM register
                              WHERE username=?''', (username,))
        temp = temp.fetchall()
    except:
        temp = []

    if temp:
        log_digest = temp[0][1] + password
        if verbosity:
            print("\nRetrieving password...")
        # Recomputing the digest for the user's salt to check the password
        for i in range(1000000):
            log_digest = hashlib.sha256(log_digest.encode('utf-8')).hexdigest()
    # Select DB row with relevant username
    try:
        rows = cursor.execute('''SELECT * from register
                              WHERE username=? AND digest=?''',
                              (username, log_digest))
        conn.commit()
        if verbosity:
            print("Done!")
        rows = rows.fetchall()
    except:
        rows = []

    # Change program behaviour based on verified registration
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

