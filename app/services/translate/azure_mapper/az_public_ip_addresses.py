def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'name'},
        'unique_id': {'call': 'createID', 'source': {
            'key': 'id',
            'reg': r'^\/subscriptions/(.*)/resourceGroups/(.*)/providers/Microsoft.Network/publicIPAddresses/(.*)?'
        }},

        'datacenters': {'call': 'fctDc',
                        'source': {**conn}},

        'environment': {'call': 'switch', 'source': 'tags.environment'},
        'ip_configuration': {'call': 'serialize', 'source': 'ip_configuration'},

        'ip_address': {'call': 'switch', 'source': 'ip_address'},
        'public_ip_address_version': {'call': 'switch', 'source': 'public_ip_address_version'},
        'type': {'call': 'switch', 'source': 'type'},
        'ddos_settings': {'call': 'switch', 'source': 'ddos_settings'},
        'dns_settings': {'call': 'serialize', 'source': 'dns_settings'},

        'family': {'call': 'setV', 'source': 'PublicIpAddress'},
        'tags': {'call': 'fctTags', 'source': 'tags'},

        'active': {'call': 'switchOptions',
                   'source': {'field': 'status',
                              'options': {},
                              'default': True
                              }},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}},
        'checksum': {'call': 'checksum',
                     'source': None}
    }
