import logging
import os

_logger = None

def setup_logger():
    global _logger
    if _logger:
        return _logger

    os.makedirs("logs", exist_ok=True)

    _logger = logging.getLogger("trading_bot")
    _logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("logs/trading_bot.log")
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    _logger.addHandler(file_handler)
    _logger.addHandler(console_handler)

    return _logger