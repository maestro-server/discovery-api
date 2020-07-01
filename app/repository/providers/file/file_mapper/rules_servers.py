def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'hostname'},
        'ipv4_private': {'call': 'switch', 'source': 'ipv4_private'},
        'ipv4_public': {'call': 'switch', 'source': 'ipv4_public'},
        'role': {'call': 'switch', 'source': 'role'},
        'environment': {'call': 'switch', 'source': 'environment'},
        'os': {'call': 'switch', 'source': 'os'},
        'services': {'call': 'switch', 'source': 'services'},
        'tags': {'call': 'switch', 'source': 'tags'},
        'cpu': {'call': 'switch', 'source': 'cpu'},
        'memory': {'call': 'switch', 'source': 'memory'},

        'auth': {'call': 'switch', 'source': 'auth'},
        'active': {'call': 'switch', 'source': 'active'},
        'status': {'call': 'switch', 'source': 'status'},

        'datacenters': {'call': 'fctDc',
                        'source': {**conn}},

        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'accountant': {'call': 'fctAccountant', 'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}},
        'checksum': {'call': 'checksum',
                     'source': None}
    }
