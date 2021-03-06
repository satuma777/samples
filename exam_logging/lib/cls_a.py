import logging

class Class_A:

    def __init__(self, filename):

        logging.basicConfig(filename=filename, level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)
        return

    def get_hello(self):

        self.logger.critical('\tHello, I\'m CRITICAL!')
        self.logger.error('\tHello, I\'m ERROR!')
        self.logger.warning('\tHello, I\'m WARNING!')
        self.logger.info('\tHello, I\'m INFO!')
        self.logger.debug('\tHello, I\'m DEBUG!')
        return
