import logging
from logging.handlers import RotatingFileHandler
import os

# Create a logger
logger = logging.getLogger("Garbage_Collector")
logger.setLevel(logging.DEBUG)

# Create the log directory if it does not exist
log_directory = "Application_logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Define the log file path
log_file_path = os.path.join(log_directory, "Garbage_Collector.log")

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a RotatingFileHandler
handler = RotatingFileHandler(log_file_path, maxBytes=2000, backupCount=5)
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(handler)
logger.addHandler(console_handler)
