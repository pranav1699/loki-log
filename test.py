import logging
 
# Create and configure logger
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
 
# Creating an object
logger = logging.getLogger()
 
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)
 
# Test messages
logger.debug("This is a debug log")
logger.warning("This is a warning log")
logger.info("This is an info log")
logger.error("This is an error log")
logger.exception("This is an exception log")