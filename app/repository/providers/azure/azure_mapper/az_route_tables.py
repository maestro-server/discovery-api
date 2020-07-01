def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'name'},
        'unique_id': {'call': 'createID', 'source': {
            'key': 'id',
            'reg': r'^\/subscriptions/(.*)/resourceGroups/(.*)/providers/Microsoft.Network/routeTables/(.*)?'
        }},

        'datacenters': {'call': 'fctDc',
                        'source': {**conn}},

        'environment': {'call': 'switch', 'source': 'tags.environment'},
        'subnets': {'call': 'serialize', 'source': 'subnets'},
        'routes': {'call': 'serialize', 'source': 'routes'},

        'disable_bgp_route_propagation': {'call': 'switch', 'source': 'disable_bgp_route_propagation'},

        'family': {'call': 'setV', 'source': 'RouteTables'},
        'tags': {'call': 'fctTags', 'source': 'tags'},

        'active': {'call': 'switchOptions',
                   'source': {'field': 'status',
                              'options': {},
                              'default': True
                              }},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'accountant': {'call': 'fctAccountant', 'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}},
        'checksum': {'call': 'checksum',
                     'source': None}
    }
