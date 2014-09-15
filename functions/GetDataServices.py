'''
Class that contains the static method for updating the daily data for a given symbol.
The csv file that contain the data is app_config.DATA_CSVS_FOLDER[$symbol].csv
The format if the csv file is:
Date,Open,High,Low,Close,Volume,Adj Close
[$YYYY-MM-dd],[$op_0],[$hp_0],[$lp_0],[$vol_0],[$adj_cp_0]
...
[$YYYY-MM-dd],[$op_N],[$hp_N],[$lp_N],[$vol_N],[$adj_cp_N]
'''
import urllib2

class GetDataServices(object):

    @staticmethod
    def get_data_from_yahoo(symbol):
        '''
        Get the historical daily data for a given symbol.
        The data is obtained from http://ichart.finance.yahoo.com/table.csv?s=[$symbol]&d=6&g=d&ignore=.csv

        :param symbol -- str, name of the symbol.
        :return: string -- The format if the string is:
        Date,Open,High,Low,Close,Volume,Adj Close
        [$YYYY-MM-dd],[$op_0],[$hp_0],[$lp_0],[$vol_0],[$adj_cp_0]
        ...
        [$YYYY-MM-dd],[$op_N],[$hp_N],[$lp_N],[$vol_N],[$adj_cp_N]
        '''
        url = "http://ichart.finance.yahoo.com/table.csv?s=" + symbol + "&d=6&g=d&ignore=.csv"

        req = urllib2.Request(url)
        return urllib2.urlopen(req).read()

