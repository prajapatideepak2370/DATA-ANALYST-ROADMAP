import inspect
import logging
class CustomLogger:
    def cust_logger(self, logLevel=logging.DEBUG):
    #Set class/method name from where its called
        logger_name = inspect.stack()[1][3]
    #create Logger    
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)
    #Create console handler or file handler and set the log level 
        fh = logging.FileHandler("FileLogs.log")
    #Create formatter - how you want your logs to be formatted
        formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s',
                     datefmt='%m/%d/%Y %I:%M:%S %p')
    # add formatter to console or file handler
        fh.setFormatter(formatter)
    # add console handler to logger
        logger.addHandler(fh)
        return logger
    
