'''
Unit Tests for the class functions.DailyDataServices. 
'''
import unittest
from functions.DailyDataServices import DailyDataServices

class  Test_DailyDataServices(unittest.TestCase):

    def runTest(self):
        '''
        Run the tests.

        :param None
        :return: None
        '''
        self.assertEqual(DailyDataServices.update_daily_data_by_symbol("AA")[0], True)
        self.assertEqual(DailyDataServices.update_daily_data_by_symbol("A2")[0], False)
        
        self.assertTrue(len(DailyDataServices.get_daily_data_by_symbol("AA")) > 0)
        self.assertTrue(len(DailyDataServices.get_daily_data_by_symbol("A2")) == 0)

        self.assertTrue(DailyDataServices.is_daily_data_by_symbol("AA")[0])
        self.assertFalse(DailyDataServices.is_daily_data_by_symbol("A2")[0])
        
        self.assertTrue(DailyDataServices.remove_daily_data_by_symbol("AA")[0])
        self.assertTrue(len(DailyDataServices.get_daily_data_by_symbol("AA")) == 0)
        self.assertEqual(DailyDataServices.update_daily_data_by_symbol("AA")[0], True)
        self.assertTrue(len(DailyDataServices.get_daily_data_by_symbol("AA")) > 0)

if __name__ == '__main__':
    unittest.main()

