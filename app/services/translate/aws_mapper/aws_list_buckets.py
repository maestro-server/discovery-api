def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'Name'},
        'created_at': {'call': 'switch', 'source': 'CreationDate'},
        'provider': {'call': 'setV', 'source': 'S3 (AWS)'},
        'family': {'call': 'setV', 'source': 'ObjectStorage'},
        'active': {'call': 'setV', 'source': True},
        'datacenters': {'call': 'fctDcApp',
                        'source': {**conn}},
        'own': {'call': 'setV', 'source': 1},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}}
    }
