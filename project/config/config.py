import logging
from logging.handlers import RotatingFileHandler
import os

logger = logging.getLogger("ChowChow")
logger.setLevel(logging.DEBUG)
log_directory = "C:\\logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

log_file_path = os.path.join(log_directory, "Chow_Chow.log")
log_file = "Chow_Chow.log"
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler = RotatingFileHandler(log_file_path, maxBytes=2000, backupCount=5)
handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

handler.setFormatter(formatter)
logger.addHandler(handler)
logger.addHandler(console_handler)