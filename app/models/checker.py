
from .validate import Validate

class Checker(object):

    def __init__(self, dc, data):
        self.dc = dc
        self.data = data

    def check(self):
        valid = Validate(self.data).validate()
        return "check"