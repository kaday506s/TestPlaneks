import logging
from datetime import datetime
from django.conf import settings


class Logger:

    @staticmethod
    def _logging(name_file):
        logger = logging.getLogger(f"{__name__}{name_file}")

        logger.addHandler(logging.FileHandler(
            f'{settings.BASE_DIR}/logs/{name_file}_'
            f'{"{:%Y-%m-%d}".format(datetime.now())}')
        )
        logger.setLevel(logging.DEBUG)
        return logger
