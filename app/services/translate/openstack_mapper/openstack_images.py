def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'name'},
        'resources_key': {'call': 'switch', 'source': 'resources_key'},
        'metadata': {'call': 'switch', 'source': 'description'},
        'size': {'call': 'switch', 'source': 'size'},
        'unique_id': {'call': 'switch', 'source': 'id'},
        'status': {'call': 'switch', 'source': 'status'},
        'progress': {'call': 'switch', 'source': 'progress'},
        'service': {'call': 'switch', 'source': 'service'},
        'min_disk': {'call': 'switch', 'source': 'min_disk'},

        'datacenters': {'call': 'fctDcApp',
                        'source': {**conn}},
        'own': {'call': 'setV', 'source': 1},
        'active': {'call': 'setV', 'source': True},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}}
    }
