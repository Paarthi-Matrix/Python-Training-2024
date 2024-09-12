import logging
from logging.handlers import RotatingFileHandler
import os
from constants.constants import LOGGER_LEVEL, LOG_FILE_PATH
from utils.trace_id_utils import get_trace_id, TraceIDFormatter


logger = logging.getLogger("BizNex")
logger.setLevel(logging.DEBUG)
log_directory = LOG_FILE_PATH
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

log_file_path = os.path.join(log_directory, "BizNex_App.log")
log_file = "BizNex_App.log"

handler = RotatingFileHandler(log_file_path, maxBytes=2000, backupCount=5)
handler.setLevel(logging.DEBUG)
formatter = TraceIDFormatter('%(asctime)s - TRACE ID: %(trace_id)s - %(name)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

handler.setFormatter(formatter)
logger.addHandler(handler)
logger.addHandler(console_handler)
