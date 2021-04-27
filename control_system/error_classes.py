class Error(Exception):
    """ Base class for exceptions in this module. """


class CommandError(Error):
    """Exception raised for errors in the command input

    Attributes:
        command -- input command in which the error was raised
        message -- explanation of why this occured
    """

    def __init__(self, command, message):
        self.command = command
        self.message = message
