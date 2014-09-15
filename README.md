stock-daily-data-webapp
=======================

Web Application that shows the daily data for a defined list if stock symbols.

This app used flask as web framework.

The application run in:
http://[$HOST]:$PORT]/ ($HOST and $PORT are defined in app_config.py).


Install
=======

See the file named INSTALL.


Files Structure
===============

Configuration
-------------
- app_config.py = configuration of the folder paths, host and post.
- logging.conf = logging configuration.
- SYMBOLS.CSV = current csv file that contains the list of stock symbols (is defined in app_cofing.SYMBOLS_CSV_FILE).

Scripts
-------
- web_server.py = Script that define the web pages and start the web server.
- update_daily_data.py = Script that update the historical daily data for a given list of symbols.
- run_tests.py = Script that run the units test defined in the tests/ folder.

Directories
-----------

a) functions/ = Clases that to real logig used by the scripts.
- GetDataServices.py = class that contains the static method for updating the daily data for a given symbol.
- DailyDataServices.py = class that contains the static methods for updating, get and remove the daily data for a given symbol.
- SymbolsManager.py = class that manage the list of symbols, this is maintained in a csv file defined in app_config.SYMBOLS_CSV_FILE.

b) csvs/ = folder where the the historical daily data are saved, is defined in app_confing.DATA_CSVS_FOLDER.

c) scripts/ = folder that contains bash scripts that run the python scripts defined in the "Scripts" section.

d) tests/ = some python unit tests.

e) static/ = contains the resources (images, js and css) used for the web views in the template folder.

f) templates/ = htmls views (used jinja2 as template engine).

