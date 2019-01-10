def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'name'},
        'unique_id': {'call': 'switch', 'source': 'id'},

        'size': {'call': 'switch', 'source': 'size_gigabytes'},
        'memory': {'call': 'switch', 'source': 'memory'},

        'fftype': {'call': 'switch', 'source': 'filesystem_type'},
        'label': {'call': 'switch', 'source': 'filesystem_label'},

        'description': {'call': 'switch', 'source': 'description'},

        'datacenters': {'call': 'fctDc',
                        'source': {**conn}},

        'created_at': {'call': 'switch', 'source': 'created_at'},
        'updated_at': {'call': 'switch', 'source': 'created_at'},

        'status': {'call': 'switchOptions',
                   'source': {'field': 'region.available',
                              'options': {},
                              'default': 'Active'
                              }},

        'active': {'call': 'setV', 'source': True},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}},
        'checksum': {'call': 'checksum',
                     'source': None}
    }
