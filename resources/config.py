import logging
from logging.handlers import RotatingFileHandler
import os
from constant.constant import LOGGER_LEVEL_DEBUG, LOG_FILE_PATH
from util.trace_id_utils import TraceIDFormatter


logger = logging.getLogger("BizNex")
logger.setLevel(LOGGER_LEVEL_DEBUG)
log_directory = LOG_FILE_PATH
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

log_file_path = os.path.join(log_directory, "BizNex_App.log")
log_file = "BizNex_App.log"

handler = RotatingFileHandler(log_file_path, maxBytes=2000, backupCount=5)
handler.setLevel(LOGGER_LEVEL_DEBUG)
formatter = TraceIDFormatter('%(asctime)s - TRACE ID: %(trace_id)s - %(name)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
console_handler.setLevel(LOGGER_LEVEL_DEBUG)
console_handler.setFormatter(formatter)

handler.setFormatter(formatter)
logger.addHandler(handler)
logger.addHandler(console_handler)
