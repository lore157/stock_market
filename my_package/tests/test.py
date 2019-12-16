import unittest
from my_package import dbmanager
import os

if __name__ == '__main__':
   unittest.main()

class Testdbmanager(unittest.TestCase):

    def setUp(self):

        dbmanager.open_and_create(0)
        dbmanager.save_new_username{'Lorenzo','123')
        f.close()

    def test_wuser(self):
        """test a wrong username"""
        u = dbmanager.check_for_username('Francesco', 'fra', 0)
        self.assertFalse(user)
    
    def test_ruser(self):
        """test a right username"""
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
    setUp()


   
