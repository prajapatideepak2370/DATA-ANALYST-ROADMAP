import logging
class loggerDemo:
    def sample_logger(self):
    #create Logger    
        logger = logging.getLogger(loggerDemo.__name__)
        logger.setLevel(logging.DEBUG)
    #Create console handler or file handler and set the log level 
        ch = logging.StreamHandler()  # show in console
        fh = logging.FileHandler("FiledemoLogs.log")
    #Create formatter - how you want your logs to be formatted
        formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s',
                     datefmt='%m/%d/%Y %I:%M:%S %p')
        formatter1 = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
    # add formatter to console or file handler
        ch.setFormatter(formatter1)
        fh.setFormatter(formatter)
    # add console handler to logger
        logger.addHandler(ch)
        logger.addHandler(fh)
    # application code - Log messages
        logger.debug("Debug log statement")
        logger.info("Info log statement")
        logger.warning("Warning log statement")
        logger.error("Error log statement")
        logger.critical("Critical log statement")

ld = loggerDemo()
ld.sample_logger()