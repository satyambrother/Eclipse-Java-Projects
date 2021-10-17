import logging
logging.basicConfig(filename='log.txt',level=logging.DEBUG)
print('python logging demo')
logging.debug("debug message")
#logging.notset("notset message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")
