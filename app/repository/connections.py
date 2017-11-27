
from .model import Model

class Connections(Model):
    state = 'warning'
    task = ''

    def markStatus(self, status, task):
        self.state = status
        self.task = task
        return self

    def markWarning(self, task):
        return self.markStatus('warning', task)

    def markSucess(self, task):
        return self.markStatus('success', task)

    def markError(self, task):
        return self.markStatus('danger', task)

    def updateState(self, msg = None):
        path = 'process.%s' % self.task
        state = {'state': self.state, 'msg': msg}
        process = {path: state}
        return self.update(process)