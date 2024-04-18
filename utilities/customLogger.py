
import logging


class LogGen():

    @staticmethod
    def loggen():
        path = '/home/karunakar/PycharmProjects/Dinero_UI_Automation/logs/logs.log'
        # logging.basicConfig(filename=path,level="DEBUG", format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        #
        # logger = logging.getLogger()
        # logger.setLevel(logging.DEBUG)
        # return logger
        # loggerName = inspect.stack()[1][3]

        logger = logging.getLogger()
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler = logging.FileHandler(path)
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger