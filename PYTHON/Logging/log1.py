# The logging module provides a flexible framework for emitting log messages from Python programs.
# Use it to configure handlers, formatters, and log levels to capture diagnostics in development and production.

# DEBUG - Detailed information, typically of interset only when diagnosing problems.
# INFO - Confirmation that things are working as expected.
# WARNING - An indication that something unexpected happend, or indicative of some problems in the near future (e.g. "disk space low"). the software is still working as expected.
# ERROR - Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL - A serious error, indicating that the program itself may be unable to continue running.

import logging
class DemoLogging:
    def add_nums(self, a, b):
        return a+b
    def mult_nums(self, a, b):
        return a * b

dl = DemoLogging()
sum_result = dl.add_nums(3, 5)
logging.info("info: addition of the numbers is: {}".format(sum_result))
logging.debug("debug: addition of the numbers is: {}".format(sum_result))
logging.error("error: addition of the numbers is: {}".format(sum_result))
logging.critical("critical: addition of the numbers is: {}".format(sum_result))
logging.warning("warning: addition of the numbers is: {}".format(sum_result))
mult_result = dl.mult_nums(3, 5)
logging.warning("The multiplication of the number is: {}".format(mult_result))
