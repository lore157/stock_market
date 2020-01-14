"""Importing the modules needed to develop the functions."""
import unittest
import os
import sys
import sqlite3
from scripts.dbmanager import open_and_create


class Test_OpenAndCreate(unittest.TestCase):
    """ Define a class to test the function open_and_create.

    The function's role in this project is to extract all registered data from
    a database or, if said database doesn't exist, create it. One test for each
    feature the function provides is inside the following class.
    """

    # Set up a blank database and corresponding cursor
    def setUp(self):
        self.mock_conn = sqlite3.connect('mock.db')
        self.mock_cursor = self.mock_conn.cursor()
        self.mock_cursor.execute('''CREATE TABLE IF NOT EXISTS 'test'
                                 (row REAL, string TEXT,
                                 PRIMARY KEY (row))''')
        self.mock_cursor.execute('''INSERT INTO test(row, string)
                                 VALUES (1, "test string") ''')

    # Test correct database creation if 'credentials.db' doesn't exist
    def test_no_register_table(self):
        quit = open_and_create('mock.db')
        self.assertRaises(SystemExit)

    # Test correct functioning of data extraction from existing database
    def test_opening_success(self):
        quit = open_and_create(None)
        self.assertEqual(None, quit)

    # Deletes mock database and connection
    def tearDown(self):
        self.mock_cursor.execute('''DROP TABLE IF EXISTS test''')
        self.mock_conn.commit()
        self.mock_cursor.close()
        self.mock_conn.close()


if __name__ == '__main__':
    unittest.main()
