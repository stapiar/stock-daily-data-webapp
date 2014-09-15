'''
Script that define the web pages and start the web server.
'''
from flask import Flask, request, jsonify, render_template, redirect
from functions.SymbolsManager import SymbolsManager
from functions.DailyDataServices import DailyDataServices
import app_config
import logging
import logging.config


'''
init app
'''
app = Flask(__name__)
logging.config.fileConfig(app_config.LOG_CONFIG_FILE)
logger = logging.getLogger()


'''
error section
'''
@app.errorhandler(400)
def bad_request():
    message = {"status":400, "message":"Bad Request"}
    resp = jsonify(message)
    resp.status_code = 400
    return resp

@app.errorhandler(500)
def internal_server_error():
    message = {"status": 500, "message":"Internal Server Error"}
    resp = jsonify(message)
    resp.status_code = 500
    return resp


'''
Web Pages
'''
@app.route("/")
def home():
    logger.info("home()")
    return render_template("home.html")

@app.route("/symbols")
def symbols():
    logger.info("symbols()")
    if "message" in request.args:
        message = request.args["message"]
    else:
        message = ""
    #get symbols
    symbols = []
    try:
        symbols_manager = SymbolsManager()
        symbols = symbols_manager.get_symbols()
    except Exception, e:
        logger.debug("symbols()", exc_info=True)
    #render template
    return render_template("symbols.html", symbols=symbols, message=message)

@app.route("/new_symbol")
def new_symbol():
    logger.info("new_symbol()")
    symbols = []
    try:
        symbols_manager = SymbolsManager()
        symbols = symbols_manager.get_symbols()
    except Exception, e:
        logger.debug("new_symbol()", exc_info=True)
    return render_template("new_symbol.html", symbols=symbols)

@app.route("/symbol_register")
def symbol_register():
    logger.info("symbol_register()")
    try:
        symbol = request.args["symbol"]
        symbols_manager = SymbolsManager()
        result = symbols_manager.add_symbol(symbol)
    except Exception, e:
        logger.debug("symbol_register()", exc_info=True)
        result = (False, "Unexpected Error")
    #check result
    if result[0]:
        message = symbol + " was create successfully."
    else:
        message = "Error in creation of " + symbol + ": " + result[1]
    return redirect("symbols?message=" + message)

@app.route("/symbol_delete")
def symbol_delete():
    logger.info("symbol_delete()")
    try:
        symbol = request.args["symbol"]
        symbols_manager = SymbolsManager()
        result = symbols_manager.remove_symbol(symbol)
        if result[0]:
            result = DailyDataServices.remove_daily_data_by_symbol(symbol)
        else:
            logger.debug("symbol_delete()", result[1])
    except Exception, e:
        logger.debug("symbol_delete()", exc_info=True)
        result = (False, "Unexpected Error")
    #check result
    if result[0]:
        message = symbol + " was deleted successfully."
    else:
        message = "Error in deletion of " + symbol + ": " + result[1]
    return redirect("symbols?message=" + message)

@app.route("/daily_curve")
def daily_curve():
    logger.info("daily_curve()")
    symbol = request.args["symbol"]
    daily_curve = []
    try:
        if DailyDataServices.is_daily_data_by_symbol(symbol):
            daily_curve = DailyDataServices.get_daily_data_by_symbol(symbol)
    except Exception, e:
        logger.debug("daily_curve()", exc_info=True)
        daily_curve = []
    return render_template("daily_curve.html", symbol=symbol, daily_curve=daily_curve)

'''
main
'''
if __name__ == "__main__":
    app.run(host=app_config.HOST, port=app_config.PORT)


