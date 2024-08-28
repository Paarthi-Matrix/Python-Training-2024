import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("BizNex")
logger.setLevel(logging.DEBUG)

log_file = "BizNex_App.log"
handler = RotatingFileHandler(log_file, maxBytes=2000, backupCount=5)
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
