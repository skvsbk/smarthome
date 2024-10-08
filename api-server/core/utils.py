
import logging
import sys
from logging import Formatter, StreamHandler

# from config import LOG_LEVEL


def get_logger(name):
    log = logging.getLogger(name)
    log.setLevel(logging.INFO)
    handler = StreamHandler(stream=sys.stdout)
    handler.setFormatter(Formatter(fmt='%(asctime)s: %(levelname)s [%(name)s] [pid-%(process)d][#%(thread)d] %(message)s'))
    log.addHandler(handler)
    return log
