def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'name'},
        'unique_id': {'call': 'switch', 'source': 'id'},
        'volume_id': {'call': 'switch', 'source': 'volume_id'},
        'service': {'call': 'switch', 'source': 'service'},
        'progress': {'call': 'switch', 'source': 'progress'},
        'project_id': {'call': 'switch', 'source': 'project_id'},
        'volume_size': {'call': 'switch', 'source': 'size'},
        'status': {'call': 'switch', 'source': 'status'},
        'created_at': {'call': 'switch', 'source': 'created_at'},
        'datacenters': {'call': 'fctDcApp',
                        'source': {**conn}},
        'own': {'call': 'setV', 'source': 1},
        'active': {'call': 'setV', 'source': True},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}}
    }
