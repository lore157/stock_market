import unittest
import os
import sys
import sqlite3
from scripts.dbmanager import open_and_create, save_new_username
from scripts.dbmanager import hash_password, check_for_username

class Test_OpenAndCreate(unittest.TestCase):
    
    # mock_conn = None
    # mock_cursor = None

    def setUp(self):
        self.mock_conn = sqlite3.connect('mock.db')
        self.mock_cursor = self.mock_conn.cursor()
        self.mock_cursor.execute('''CREATE TABLE IF NOT EXISTS 'test'
                                 (row REAL, string TEXT,
                                 PRIMARY KEY (row))''')
        self.mock_cursor.execute('''INSERT INTO test(row, string)
                                 VALUES (1, "test string") ''')

    def test_no_register_table(self):
        quit = open_and_create('mock.db')
        self.assertRaises(SystemExit)

    def test_opening_success(self):
        quit = open_and_create(None)
        self.assertEqual(None, quit)

    def tearDown(self):
        self.mock_cursor.execute('''DROP TABLE IF EXISTS test''')
        self.mock_conn.commit()
        self.mock_cursor.close()
        self.mock_conn.close()


'''    def test_wrong_user(self):
        """test a wrong username"""
        u = dbmanager.check_for_username('Francesco', 'fra', 0)
        self.assertFalse(user)
    
    def test_valid_user(self):
        """test a valid username"""
        u = dbmanager.check_for_username('Lorenzo', '123', 2)
        self.assertFalse(user)
    
    def test_empty_user(self):
        """test with an empty user"""
        u = dbmanager.check_for_username("", "")
        self.assertFalse(u)
   
    def test_mismatched_user(self):
        """testing with a user with wrong password"""
        u = dbmanager.check_for_username("Lorenzo", "ciao_sono_lorenzo")
        self.assertFalse(u)

    def tearDown(self):
        os.remove('./credentials.db') 
    
'''

if __name__ == '__main__':
   unittest.main()
   
