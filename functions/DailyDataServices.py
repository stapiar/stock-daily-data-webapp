'''
Class that contains the static methods for updating, get and remove the daily data for a given symbol.
The csv file that contain the data is app_config.DATA_CSVS_FOLDER[$symbol].csv
The format if the csv file is:
Date,Open,High,Low,Close,Volume,Adj Close
[$YYYY-MM-dd],[$op_0],[$hp_0],[$lp_0],[$vol_0],[$adj_cp_0]
...
[$YYYY-MM-dd],[$op_N],[$hp_N],[$lp_N],[$vol_N],[$adj_cp_N]
'''
import app_config
from pandas import read_csv
from functions.GetDataServices import GetDataServices
import os.path
import os
from datetime import datetime


class DailyDataServices(object):

    @staticmethod
    def get_daily_data_by_symbol(symbol):
        '''
        Get the historical daily data for a given symbol.

        :param symbol -- str, name of the symbol.
        :return: list of dict -- list, dict with the following format {"Close":$Adj_Close_i, "Date":datetime.datetime}
        '''
        try:
            data_list = read_csv(app_config.DATA_CSVS_FOLDER + symbol + ".csv", index_col=True)
            datas = [{"Close":row[1]["Adj Close"], \
            "Date":datetime(int(row[1]["Date"][:4]), int(row[1]["Date"][5:-3]), int(row[1]["Date"][-2:])).strftime("%s") + "000"\
            } for row in data_list.iterrows()]
            datas.reverse()
            return datas
        except Exception, e:
            import logging
            import logging.config
            logging.config.fileConfig(app_config.LOG_CONFIG_FILE)
            logger = logging.getLogger()
            logger.error("Error in get_daily_data_by_symbol", exc_info=True)
            return []

    @staticmethod
    def update_daily_data_by_symbol(symbol):
        '''
        function that update the historical daily data for a given symbol.
        Return False if there a error.

        :param symbol -- str, name of the symbol.
        :return: (bool, str)
        '''
        try:
            DOC = GetDataServices.get_data_from_yahoo(symbol)
            #save DOC to file
            f = open(app_config.DATA_CSVS_FOLDER + symbol + ".csv", "w")
            f.write(DOC)
            f.close()
        except Exception, e:
            return (False, str(e))
        #return
        return (True, "OK")

    @staticmethod   
    def is_daily_data_by_symbol(symbol):
        '''
        determine if there is a the historical daily data for a given symbol.

        :param symbol -- str, name of the symbol.
        :return: bool
        '''
        #return
        return (os.path.isfile(app_config.DATA_CSVS_FOLDER + symbol + ".csv"), "OK")

    @staticmethod   
    def remove_daily_data_by_symbol(symbol):
        '''
        function that the historical daily data for a given symbol from the system.
        Return False if there a error.

        :param symbol -- str, name of the symbol.
        :return: (bool, str)
        '''
        try:
            if DailyDataServices.is_daily_data_by_symbol(symbol)[0]:
                os.remove(app_config.DATA_CSVS_FOLDER + symbol + ".csv")
        except Exception, e:
           return (False, str(e)) 
        #return
        return (True, "OK")
