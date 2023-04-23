import logging
from log.custom_formatter import CustomFormatter
import environment

class Logger:
    """A custom class to initialize and configure the logging system"""

    def __init__(self, logger_name):
        """Initialize the logger with a given name and log level"""

        level = logging.DEBUG if environment.get('PYTHON_ENV') == "development" else logging.INFO
        
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(level)

        formatter = CustomFormatter('[%(name)s] - %(message)s')

        handler = logging.StreamHandler()
        handler.setLevel(level)
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

    def get_logger(self):
        """Return the logger object"""

        return self.logger