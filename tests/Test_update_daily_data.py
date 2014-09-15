'''
Unit Tests for the method update_daily_data in update_daily_data.py. 
'''
import unittest
from update_daily_data import update_daily_data

class  Test_update_daily_data(unittest.TestCase):

    def runTest(self):
        '''
        Run the tests.

        :param None
        :return: None
        '''
        self.assertIsNone(update_daily_data(["ZUMZ", "ZZ"], 20))

if __name__ == '__main__':
    unittest.main()

