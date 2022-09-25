import logging
import sys

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s:[%(levelname)s]: %(message)s"
)

LOGGER = logging.getLogger("agenda-LOGGER")
LOGGER.setLevel(logging.INFO)
LOGGER.addHandler(logging.StreamHandler(sys.stdout))


class Logging:
    @staticmethod
    def error(message=None):
        return LOGGER.error(message)

    @staticmethod
    def warning(message=None):
        return LOGGER.warning(message)

    @staticmethod
    def info(message=None):
        return LOGGER.info(message)

    @staticmethod
    def debug(message=None):
        return LOGGER.debug(message)
