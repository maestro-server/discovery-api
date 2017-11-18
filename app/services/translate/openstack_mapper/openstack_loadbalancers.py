def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'name'},
        'created_at': {'call': 'switch', 'source': 'created_at'},
        'provider': {'call': 'setV', 'source': 'OpenStack (HaProxy)'},
        'own': {'call': 'setV', 'source': 1},
        'family': {'call': 'setV', 'source': 'Loadbalance'},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}}
    }
