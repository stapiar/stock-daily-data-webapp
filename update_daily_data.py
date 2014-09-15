'''
Script that update the historical daily data for a given list of symbols. 

Usage:
python update_daily_data.py [--symbols symbol_0,...,symbol_N] [--retries int_value]

Examples:
python update_daily_data.py --symbols ZUMZ,ZZ --retries 20
python update_daily_data.py --symbols ZUMZ,ZZ
python update_daily_data.py --retries 20
python update_daily_data.py
'''
from functions.SymbolsManager import SymbolsManager
from functions.DailyDataServices import DailyDataServices
import argparse
import app_config
import logging
import logging.config


def update_daily_data(symbols, retries):
    '''
    Functions that update the historical daily data for a given list of symbols, 
    using a number of the retries if the isn't successfully updated.

    :param symbols -- list of str, names of the symbols.
    :param retries -- int, number of the retries if the isn't successfully update.
    :return: None
    '''
    logging.config.fileConfig(app_config.LOG_CONFIG_FILE)
    logger = logging.getLogger()
    logger.info("START update_daily_data")
    for symbol in symbols:
        #update $symbol
        counter = 0
        while counter < retries:
            if DailyDataServices.update_daily_data_by_symbol(symbol)[0]:
                #update counter
                counter = retries
            else:
                logger.info("ERROR " + symbol)
            counter += 1
        #check if successfully updated.
        if counter > retries:
            logger.info(symbol + " OK")
        else:
            logger.info(symbol + " NO_DATA")
    logger.info("FINAL update_daily_data")

if __name__ == "__main__":
    '''
    Examples:
    python update_daily_data.py --symbols ZUMZ,ZZ --retries 20
    python update_daily_data.py --symbols ZUMZ,ZZ
    python update_daily_data.py --retries 20
    '''
    #args
    parser = argparse.ArgumentParser(description="Update Daily Data")
    parser.add_argument("-s", "--symbols", help="symbol_0,...,symbol_N", default=None)
    parser.add_argument("-r", "--retries", help="int value", default="20")
    args = parser.parse_args()
    #set params
    if args.symbols == None:
        symbols_manager = SymbolsManager()
        args.symbols = symbols_manager.get_symbols()
    else:
        args.symbols = args.symbols.split(",")        
    if args.retries.isdigit():
        args.retries = int(args.retries)
        #update_daily_data
        update_daily_data(args.symbols, args.retries)
    else:
        print ("retries shouid be int.")


