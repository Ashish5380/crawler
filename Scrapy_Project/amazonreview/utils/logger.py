import logging
import logging.handlers

# task logger
LOG_FILENAME = '/opt/akoshalogs/amazoncrawler.log'
logger = logging.getLogger('Logger')
logger.setLevel(logging.INFO)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s")
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=20000000, backupCount=5)
handler.setFormatter(file_formatter)
logger.addHandler(handler)