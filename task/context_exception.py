import traceback


class ArgumentException(Exception):
    def __init__(self, arguments, message='Gotten argument, is not valid'):
        self.arguments = arguments
        self.message = message
        super().__init__(message)

    def __str__(self):
        return "{} : {}".format(self.arguments, self.message)
