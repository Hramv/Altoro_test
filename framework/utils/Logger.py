import logging
import sys


def new_line(log_method_function: object) -> object:

    """
    The decorator function to add new line in logs.

    Parameters
    ----------
    log_method_function: object
        Logging function for exact log level.
    """

    def add_new_line(message):
        log_method_function(message=message)

    return add_new_line


class Logger(object):

    """
    Utility for logging actions.

    Attributes
    ----------
    __logger: Logger
        Logger with the specified name.

    Methods
    -------
    set_level(level)
        Set the logging level of this logger. Level must be an int or a str.
    """

    __logger = logging.getLogger("Logger")
    logging.basicConfig(level=logging.INFO,
                        stream=sys.stdout, 
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%d-%m-%y %H:%M:%S')

    @staticmethod
    def set_level(level) -> None: # type: ignore

        """
        Set the logging level of this logger. 
        
        Parameters
        ----------
        issuer: str
            An int or a str level of logging.
        """

        Logger.__logger.setLevel(level)


    @staticmethod
    @new_line
    def info(message: str) -> None:

        """
        Writes a log with 'info' level. 
        
        Parameters
        ----------
        message: str
            Message to log.
        """

        Logger.__logger.info(msg=message)


    @staticmethod
    @new_line
    def debug(message) -> None:

        """
        Writes a log with 'debug' level. 
        
        Parameters
        ----------
        message: str
            Message to log.
        """

        Logger.__logger.debug(msg=message)


    @staticmethod
    @new_line
    def warning(message) -> None:

        """
        Writes a log with 'warning' level. 
        
        Parameters
        ----------
        message: str
            Message to log.
        """

        Logger.__logger.warning(msg=message)


    @staticmethod
    @new_line
    def error(message) -> None:

        """
        Writes a log with 'error' level. 
        
        Parameters
        ----------
        message: str
            Message to log.
        """

        Logger.__logger.error(msg=message)