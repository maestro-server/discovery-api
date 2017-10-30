
from .model import Model

class Providers(Model):
    state = 'warning'
    task = ''

    def markWarning(self, task):
        self.state = 'warning'
        self.task = task
        return self

    def markSucess(self, task):
        self.state = 'success'
        self.task = task
        return self

    def markError(self, task):
        self.state = 'error'
        self.task = task
        return self

    def updateState(self, msg = None):
        path = 'process.%s' % self.task
        state = {'state': self.state, 'msg': msg}
        process = {path: state}
        return self.update(process)