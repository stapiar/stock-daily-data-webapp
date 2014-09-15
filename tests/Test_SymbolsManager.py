'''
Unit Tests for the class functions.SymbolsManager. 
'''
import unittest
from functions.SymbolsManager import SymbolsManager

class  Test_SymbolsManager(unittest.TestCase):

    def runTest(self):
        '''
        Run the tests.

        :param None
        :return: None
        '''
        symbols_manager = SymbolsManager()
        symbols = symbols_manager.get_symbols()

        self.assertTrue(len(symbols) > 0)
        
        self.assertIsNone(symbols_manager.save_symbols_to_csv())

        self.assertEqual(symbols_manager.remove_symbol("AA")[0], True)
        self.assertFalse("AA" in symbols_manager.get_symbols())

        self.assertEqual(symbols_manager.add_symbol("AA")[0], True)
        self.assertTrue("AA" in symbols_manager.get_symbols())

if __name__ == '__main__':
    unittest.main()

