import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from api_caller import fetchApiData


class TestAPIVerification(unittest.TestCase):
    # This sends in an invalid stock symbol and makes sure the functino handles it and returns the proper outputs
    def test_checkApiCall(self):
        self.assertEqual(fetchApiData("Invalid_Ticker_Sign"), (False, None))

unittest.main()