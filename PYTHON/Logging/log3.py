import logging
logging.basicConfig(level=logging.DEBUG,
                     filename="DebugDemo.log", filemode="a",
                     format='%(asctime)s - %(levelname)s : %(message)s',
                     datefmt='%m/%d/%Y %I:%M:%S %p'  )
class DemoLogging:
    def add_nums(self, a, b):
        return a+b
    def mult_nums(self, a, b):
        return a * b

dl = DemoLogging()
sum_result = dl.add_nums(3, 5)
logging.debug("debug: addition of the numbers is: {}".format(sum_result))
logging.info("info: addition of the numbers is: {}".format(sum_result))
logging.error("error: addition of the numbers is: {}".format(sum_result))
logging.critical("critical: addition of the numbers is: {}".format(sum_result))
logging.warning("warning: addition of the numbers is: {}".format(sum_result))
mult_result = dl.mult_nums(3, 5)
logging.warning("The multiplication of the number is: {}".format(mult_result))