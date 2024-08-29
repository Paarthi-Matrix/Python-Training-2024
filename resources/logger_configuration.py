
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("Garbage_Collector")
logger.setLevel(logging.DEBUG)

log_file = "Garbage_Collector.log"
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler = RotatingFileHandler(log_file, maxBytes=2000, backupCount=5)
handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

handler.setFormatter(formatter)
logger.addHandler(handler)
logger.addHandler(console_handler)
