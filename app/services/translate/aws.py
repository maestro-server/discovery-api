

from .mapper import Mapper

class MapperAWS(Mapper):

    def translate(self, data):
        data = data['Instances'][0]
        translate = {}

        oper = self.mapp()
        for key, item in oper.items():
            res = getattr(self, item['call'])(item['source'], data)

            if not res == None:
                translate[key] = res
                print("translate", res)

        return translate

    def mapp(self):
        mapper = {
            'describe_instances': {
                'hostname': {'call': 'arrCatcher',
                             'source': {'field': 'Tags', 'sKey': 'Key', 's': 'name', 'catcher': 'Value'}},
                'role': {'call': 'arrCatcher',
                             'source': {'field': 'Tags', 'sKey': 'Key', 's': 'role', 'catcher': 'Value'}},
                'environment': {'call': 'arrCatcher',
                         'source': {'field': 'Tags', 'sKey': 'Key', 's': 'environment', 'catcher': 'Value'}},
                'created_at': {'call': 'switch', 'source': 'LaunchTime'},
                'ipv4_private': {'call': 'switch', 'source': 'PrivateIpAddress'},
                'ipv4_public': {'call': 'switch', 'source': 'PublicIpAddress'},
                'dns_public': {'call': 'switch', 'source': 'PublicDnsName'},
                'storage': {'call': 'fctStorage', 'source': 'BlockDeviceMappings'},
                'auth': {'call': 'fctAuth', 'source': 'KeyName'}
            }
        }

        return mapper[self.command]