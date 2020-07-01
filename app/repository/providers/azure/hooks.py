import json
from pydash.objects import get
from app.services.factory import FactoryAPI
from app.libs.decodeConn import decodeConn

from app.repository.externalMaestroData import ExternalMaestroData
from app.libs.cache import CacheMemory


class HookedAzure(object):
    _conn = None

    @staticmethod
    def createConn(conn):
        if HookedAzure._conn == None:
            access = decodeConn(conn, conn.get('_id'), "hooked ipv4")
            Crawler = FactoryAPI(access=access, conn=conn)
            HookedAzure._conn = Crawler

        return HookedAzure._conn

    @staticmethod
    def ipv4(obj, conn, len):
        Crawler = HookedAzure.createConn(conn)
        options = {
            "access": "network_interfaces",
            "command": "network",
            "result_path": "value",
            "conf": {"exec": "get"}
        }

        for interface in obj.get('network_interface'):
            name = " ".join(interface['id'].split('/')[-1:])
            sub = "".join(interface['id'].split('/')[4])

            vars = [
                {"resource_group_name": sub},
                {"network_interface_name": name}
            ]

            result = Crawler.execute(options, vars)
            ips = get(result, 'result.ip_configurations')

            for ip in ips:
                if hasattr(ip, len):
                    return getattr(ip, len)

    @staticmethod
    def ipv4Private(obj, conn):
        return HookedAzure.ipv4(obj, conn, 'private_ip_address')

    @staticmethod
    def ipv4Public(obj, conn):
        ip_reference = HookedAzure.ipv4(obj, conn, 'public_ip_address')
        ip_reference = ip_reference.id.split('/')

        Crawler = HookedAzure.createConn(conn)
        options = {
            "access": "public_ip_addresses",
            "command": "network",
            "result_path": "value",
            "conf": {"exec": "get"}
        }

        vars = [
            {"resource_group_name": ip_reference[4]},
            {"public_ip_address_name": ip_reference[8]}
        ]

        result = Crawler.execute(options, vars)
        return get(result, 'result.ip_address')

    @staticmethod
    def cpuAndMemoryByInstanceType(obj, conn):
        instance = get(obj, 'datacenters.instance')

        if instance:
            data = CacheMemory.get(instance)
            if not data:
                query = json.dumps({'size': instance})

                result = ExternalMaestroData() \
                    .post_request(path="flavors_public", body={'query': query}) \
                    .get_results('items')

                if result:
                    content = get(result, '[0]')
                    vcpus = get(content, 'vcpu')
                    memory = get(content, 'memory_gib')

                    if vcpus and memory:
                        data = {
                            'cpu': int(vcpus),
                            'memory': float(memory),
                        }

                        CacheMemory.set(instance, data)

            return data
