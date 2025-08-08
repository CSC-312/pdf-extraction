import sys
from loguru import logger


def get_logger():
    logger.remove()
    logger.add(sink=sys.stdout, format="<green>{level}</green>: {message}")
    return logger
