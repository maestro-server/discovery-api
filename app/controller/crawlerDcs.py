
from flask_restful import Resource
from app.models.adminer import Adminer

from app.tasks.tasks import add

class CrawlerDcs(Resource):
    def get(self, datacenter):

        x =10
        y = 5
        res = add.apply_async((x, y))
        context = {"id": res.task_id, "x": x, "y": y}
        result = "add((x){}, (y){})".format(context['x'], context['y'])
        goto = "{}".format(context['id'])
        return {result: result, goto:goto}

        path = '.permissions.%s' % datacenter
        return Adminer().getOptions('providers', path)