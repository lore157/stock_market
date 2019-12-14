import unittest
from stock_market.main import readCompaniesCsv
import os

class TestreadCompaniesCsv(unittest.TestCase):
    
    def setUp(self):
    """creating a temporary file to test our function"""
        self.temporary_file = "/tmp/emptyfile"
        f = open(self.temporary_file, 'w')
        f.close()

    def test_no_datafile(self):
    """testing with no datafile"""
        df = readCompaniesCsv(path="/tmp/nonexistentfile-wewefwwe")
        self.assertFalse(df)        

    def test_empty_datafile(self):
    """testing with an empty file"""
        df = readCompaniesCsv(path=self.temporary_file)
        self.assertFalse(df)

    def test_csv_file(self):
    """testing a file that is not a csv"""
        df = readCompaniesCsv(path=self.temporary_file)
        self.assertFalse(df)

    def tearDown(self):
    os.remove(self.temporary_file)
    setUp()

from scripts.dbmanager import check_for_username

class Testdbmanager(unittest.TestCase):

    def setUp(self):
        global conn
        global cursor
        conn = sqlite3.connect('credentials.db')
        cursor = conn.cursor()

    def test_non_existing_user(self):
    """test with a non existing user"""
        res = dbmanager.check_for_username("Giulio Cesare", "Ave")
        self.assertFalse(res)

    def test_empty_user(self):
    """test with an empty user"""
        res = dbmanager.check_for_username("", "")
        self.assertFalse(res)

    def test_mismatched_user(self):
    """testing with a user with wrong password"""
        res = dbmanager.check_for_username("Lorenzo", "ciao_sono_lorenzo")
        self.assertFalse(res)

    def test_correct_user(self):
    """testing a correct user"""
        res = github.check_for_username("Lorenzo", "123", 
                                verbose=True)
        self.assertTrue(res)


