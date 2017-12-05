def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'name'},
        'unique_id': {'call': 'switch', 'source': 'id'},
        'created_at': {'call': 'switch', 'source': 'created_at'},
        'provider': {'call': 'setV', 'source': 'OpenStack (HaProxy)'},
        'own': {'call': 'setV', 'source': 1},
        'family': {'call': 'setV', 'source': 'Loadbalance'},
        'datacenters': {'call': 'fctDcApp',
                        'source': {**conn}},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'active': {'call': 'setV', 'source': True},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}}
    }
