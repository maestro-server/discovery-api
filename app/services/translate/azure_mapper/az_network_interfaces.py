def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'name'},
        'unique_id': {'call': 'createID', 'source': {
            'key': 'id',
            'reg': r'^\/subscriptions/(.*)/resourceGroups/(.*)/providers/Microsoft.Network/networkInterfaces/(.*)?'
        }},

        'datacenters': {'call': 'fctDc',
                        'source': {**conn}},

        'created_at': {'call': 'now'},
        'updated_at': {'call': 'now'},

        'environment': {'call': 'switch', 'source': 'tags.environment'},
        'ip_configurations': {'call': 'serialize', 'source': 'ip_configurations'},

        'mac_address': {'call': 'switch', 'source': 'mac_address'},
        'resource_guid': {'call': 'switch', 'source': 'resource_guid'},
        'type': {'call': 'switch', 'source': 'type'},
        'enable_ip_forwarding': {'call': 'switch', 'source': 'enable_ip_forwarding'},
        'dns_settings': {'call': 'serialize', 'source': 'dns_settings'},

        'family': {'call': 'setV', 'source': 'NetworkInterface'},
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
