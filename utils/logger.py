import logging
import os


def get_logger():

    os.makedirs("reports", exist_ok=True)

    logger = logging.getLogger(__name__)

    if not logger.handlers:

        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler("reports/test.log")

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger