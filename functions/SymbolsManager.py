'''
Class that manage the list of symbols, this is maintained in a csv file defined in app_config.SYMBOLS_CSV_FILE.
'''
import app_config
from pandas import read_csv, DataFrame 


class SymbolsManager(object):

    symbol_list = []

    def __init__(self):
        '''
        Read the symbols param from the csv file defined in app_config.SYMBOLS_CSV_FILE.
        param symbols: pandas.core.frame.DataFrame, Data columns: symbol.
        '''
        self.symbols = read_csv(app_config.SYMBOLS_CSV_FILE)

    def get_symbols(self):
        '''
        Get a list of strings (symbols in the system).

        :param None
        :return: list of string.
        '''
        return [row[1]["symbol"] for row in self.symbols.iterrows()]
    
    def save_symbols_to_csv(self):
        '''
        Save the symbols param to the csv file defined in app_config.SYMBOLS_CSV_FILE. 
        param symbols: pandas.core.frame.DataFrame, Data columns: symbol.
        '''        
        with open(app_config.SYMBOLS_CSV_FILE, "w") as f:
            self.symbols.to_csv(f, header=True, index=False)    

    def remove_symbol(self, symbol):
        '''
        function that remove a symbol from the system.
        Return False if there a error.

        :param symbol -- str, name of the symbol.
        :return: (bool, str)
        '''
        self.symbols = self.symbols[self.symbols["symbol"] != symbol]
        self.save_symbols_to_csv()
        #return
        return (True, "OK")

    def add_symbol(self, symbol):
        '''
        function that add a symbol to the system.
        Return False if there a error.

        :param symbol -- str, name of the symbol.
        :return: (bool, str)
        '''
        if symbol not in self.symbols:
            self.symbols = self.symbols.append(DataFrame([symbol], columns=["symbol"])).sort(columns="symbol")
            self.save_symbols_to_csv()
        #return
        return (True, "OK")
    
    