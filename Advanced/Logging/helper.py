''' 

making a module callled helper which makes a helper info logging which when used in the Logging.py

'''

# importing the logging 

import logging
logger=logging.getLogger(__name__)


# if we use logging.propagate it does is that it make the next logger not work 
logger.propagate=False
logger.info('hello')