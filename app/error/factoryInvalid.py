


class FactoryInvalid(object):

    @staticmethod
    def responseInvalid(msg, code=400):
        return {'error': msg}, code