import logging


class Logger(object):
    __instance = None

    def __init__(self):
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    @classmethod
    def get_instance(cls):
        """
        Get logger instance
        Returns:
            logger instance
        """
        if not cls.__instance:
            cls.__instance = Logger()
        return cls.__instance

    def info(self, msg):
        logging.info(msg=msg)

    def warning(self, msg):
        logging.warning(msg=msg)

    def debug(self, msg):
        logging.debug(msg=msg)

    def error(self, msg):
        logging.error(msg=msg)

    def critical(self, msg):
        logging.critical(msg=msg)

    def log_step(self, number, step_name):
        """
        Log step of test
        Args:
            number: number of step
            step_name: step name
        """
        self.info(msg='--- STEP {0}: {1}'.format(number, step_name))
