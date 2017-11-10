

from .mapper import Mapper
from app.services.rules.aws import RulerAWS

class MapperAWS(Mapper):

    def translate(self, data):
        data = data['Instances'][0]
        translate = {}

        oper = self.mapp()
        for key, item in oper.items():
            res = getattr(RulerAWS, item['call'])(item['source'], data)

            if not res == None:
                translate[key] = res

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
                'dns_private': {'call': 'switch', 'source': 'PrivateDnsName'},
                'storage': {'call': 'fctStorage', 'source': 'BlockDeviceMappings'},
                'auth': {'call': 'fctAuth', 'source': 'KeyName'},
                'tags': {'call': 'fctTags', 'source': 'Tags'},
                'ebs_optimized': {'call': 'switch', 'source': 'EbsOptimized'},
                'status': {'call': 'switchOptions',
                           'source': {'field': 'State.Name',
                                      'options': {'running': 'Active', 'pending': 'Active', 'stopping': 'Avaliable', 'stopped': 'Avaliable'},
                                      'default': None
                                      }},
                'active': {'call': 'switchOptions',
                           'source': {'field': 'State.Name',
                                      'options': {'shutting-down': False, 'terminated': False},
                                      'default': True
                                      }},
                'datacenters': {'call': 'fctDc',
                                'source': {**self.conn}}
            }
        }

        return mapper[self.command]