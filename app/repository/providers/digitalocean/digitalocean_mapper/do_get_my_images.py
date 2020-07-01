def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'name'},
        'unique_id': {'call': 'switch', 'source': 'id'},

        'distribution': {'call': 'switch', 'source': 'distribution'},
        'slug': {'call': 'switch', 'source': 'slug'},

        'public': {'call': 'switch', 'source': 'public'},
        'regions': {'call': 'switch', 'source': 'regions'},

        'min_disk_size': {'call': 'switch', 'source': 'min_disk_size'},
        'type': {'call': 'switch', 'source': 'type'},

        'size': {'call': 'switch', 'source': 'size_gigabytes'},
        'description': {'call': 'switch', 'source': 'description'},

        'datacenters': {'call': 'fctDc',
                        'source': {**conn}},

        'created_at': {'call': 'switch', 'source': 'created_at'},
        'updated_at': {'call': 'switch', 'source': 'created_at'},

        'status': {'call': 'switchCapitalized', 'source': 'status'},
        'active': {'call': 'switchOptions',
                   'source': {'field': 'status',
                              'options': {
                                  "deleted": False},
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
