import logging
import os
from logging.handlers import RotatingFileHandler


from constant.constant import LOG_FILE, LOG_FORMATTER


def check_directory(directory_path):
    """Ensure that a directory exists; create it if it does not."""
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)


def setup_logger():
    """configuring logging for both log file and stream in console"""
    log_dir = "logs"
    check_directory(log_dir)

    log_file_path = os.path.join(log_dir, LOG_FILE)

    logger = logging.getLogger("lending_system")
    logger.setLevel(logging.DEBUG)

    if logger.hasHandlers():
        logger.handlers.clear()

    file_handler = RotatingFileHandler(log_file_path, maxBytes=2*1024*1024, backupCount=2)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(LOG_FORMATTER))

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(LOG_FORMATTER))

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
