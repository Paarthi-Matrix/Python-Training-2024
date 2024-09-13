import logging
from logging.handlers import RotatingFileHandler
import os

from helper.constant import LOG_FILE_LOCATION

logger = logging.getLogger("Garbage_Collector")
logger.setLevel(logging.DEBUG)

# Define log directory and file path
log_directory = LOG_FILE_LOCATION
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

log_file_path = os.path.join(log_directory, "Garbage_Collector.log")

# Define formatter for file (includes traceback)
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s\n%(exc_info)s')

# Define formatter for console (no traceback)
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a RotatingFileHandler for file logging
file_handler = RotatingFileHandler(log_file_path, maxBytes=2000, backupCount=5)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(file_formatter)

# Create a StreamHandler for console logging
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(console_formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

