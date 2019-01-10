def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'name'},
        'unique_id': {'call': 'switch', 'source': 'id'},

        'role': {'call': 'batch',
                 'source': {
                     'region': {'call': 'switch', 'source': 'region'},
                     'endpoint': {'call': 'switch', 'source': 'endpoint'},
                     'version': {'call': 'switch', 'source': 'version'},
                     'ipv4': {'call': 'switch', 'source': 'ipv4'},
                     'cluster_subnet': {'call': 'switch', 'source': 'cluster_subnet'},
                     'service_subnet': {'call': 'switch', 'source': 'service_subnet'},
                     'node_pools': {'call': 'switch', 'source': 'node_pools'}
                 }
                 },

        'datacenters': {'call': 'fctDc',
                        'source': {**conn}},

        'created_at': {'call': 'switch', 'source': 'created_at'},
        'updated_at': {'call': 'switch', 'source': 'created_at'},

        'status': {'call': 'switch', 'source': 'status'},
        'active': {'call': 'switchOptions',
                   'source': {'field': 'status',
                              'options': {
                                  "errored": False},
                              'default': True
                              }},

        'provider': {'call': 'setV', 'source': 'Kubernetes (DigitalOcean)'},
        'own': {'call': 'setV', 'source': 1},
        'family': {'call': 'setV', 'source': 'ContainerOrchestration'},

        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}},
        'checksum': {'call': 'checksum',
                     'source': None}
    }
