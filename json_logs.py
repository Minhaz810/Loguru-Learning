import sys
from loguru import logger

"""Formatting"""
# logger.add(sys.stdout,format="{time} {level}---{message}") # with default configuration, two output
logger.remove()
logger.add(
    sys.stdout,format="{time:MMMM D ,YYYY HH:mm:ss} {level}---<level>{message}</level>",
    serialize= True
)

logger.info("An info message")
logger.error("An error occured")
logger.critical("This is a critical error")