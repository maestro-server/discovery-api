def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'Name'},
        'unique_id': {'call': 'switch', 'source': 'Name'},

        'created_at': {'call': 'switch', 'source': 'CreationDate'},

        'provider': {'call': 'setV', 'source': 'Spaces (DigitalOcean)'},
        'family': {'call': 'setV', 'source': 'ObjectStorage'},
        'active': {'call': 'setV', 'source': True},
        'own': {'call': 'setV', 'source': 1},

        'datacenters': {'call': 'fctDcBuckets',
                        'source': {**conn}},

        'status': {'call': 'switch', 'source': 'status'},
        'active': {'call': 'switchOptions',
                   'source': {'field': 'status',
                              'options': {
                                  "deleted": False},
                              'default': True
                              }},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}},
        'checksum': {'call': 'checksum',
                     'source': None}
    }
