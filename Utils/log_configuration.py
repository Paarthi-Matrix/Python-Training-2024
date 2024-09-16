import logging
import os

from logging.handlers import RotatingFileHandler
from Utils.constants import LOG_FILE, LOG_FORMATTER


def setup_logger():
    """configuring logging for both log file and stream in console"""
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file_path = os.path.join(log_dir, LOG_FILE)

    logger = logging.getLogger("lending_system")
    logger.setLevel(logging.DEBUG)

    file_handler = RotatingFileHandler(LOG_FILE, maxBytes=2*1024*1024, backupCount=2)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(LOG_FORMATTER))

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(LOG_FORMATTER))

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
