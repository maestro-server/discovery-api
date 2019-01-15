import re
import json
from pydash.objects import get

from app.repository.externalMaestroData import ExternalMaestroData
from app.libs.cache import CacheMemory


class HookedAWS(object):

    @staticmethod
    def cpuAndMemoryByInstanceType(obj, conn):
        instance = get(obj, 'datacenters.instance')

        if instance:
            data = CacheMemory.get(instance)
            if not data:
                query = json.dumps({'api_name': instance})

                result = ExternalMaestroData() \
                    .post_request(path="flavors_public", body={'query': query}) \
                    .get_results('items')

                if result:
                    content = get(result, '[0]')
                    vcpus = get(content, 'vcpus')
                    memory = get(content, 'memory')

                    if vcpus and memory:
                        data = {
                            'cpu': re.search(r'([0-9]*)', vcpus).group(),
                            'memory': re.search(r'([0-9\.]*)', memory).group(),
                        }

                        CacheMemory.set(instance, data)

            return data
