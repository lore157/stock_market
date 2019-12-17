import unittest
import os
import sys
import sqlite3
from scripts.dbmanager import open_and_create, save_new_username
from scripts.dbmanager import hash_password, check_for_username


# Test the function that extracts data from a table or creates it.
class Test_OpenAndCreate(unittest.TestCase):

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


if __name__ == '__main__':
   unittest.main()
   
