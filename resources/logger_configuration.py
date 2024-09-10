import logging
from logging.handlers import RotatingFileHandler
import os

from helper.constant import LOG_FILE_LOCATION

logger = logging.getLogger("Garbage_Collector")
logger.setLevel(logging.INFO)


log_directory = LOG_FILE_LOCATION
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

log_file_path = os.path.join(log_directory, "Garbage_Collector.log")

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a RotatingFileHandler
handler = RotatingFileHandler(log_file_path, maxBytes=2000, backupCount=5)
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

logger.addHandler(handler)
logger.addHandler(console_handler)
