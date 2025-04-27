import unittest
import os

# Got this through research and fount it is the best way to import a function 
# from a file that is a level above the test folder
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db_handler import createDB


class TestDatabaseCreation(unittest.TestCase):
    def setUp(self):
        if os.path.exists("FinalProject.db"):
            os.remove('FinalProject.db')

    # Check that the file creation was good
    def test_file_creation(self):
        createDB()
        self.assertTrue(os.path.exists("FinalProject.db"))


unittest.main()


