
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class ClientMaestroError(Error):

    def __init__(self, msg):
        self.msg = msg