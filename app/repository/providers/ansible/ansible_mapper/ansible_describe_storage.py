def rules(conn):
    return {
        'unique_id': {'call': 'getUniqueId', 'source': ''},
        'size': {'call': 'getSize', 'source': 'size'},

        'sectors': {'call': 'switch', 'source': 'sectors'},
        'sectorsize': {'call': 'switch', 'source': 'sectorsize'},
        'support_discard': {'call': 'switch', 'source': 'support_discard'},
        'model': {'call': 'switch', 'source': 'model'},
        'host': {'call': 'switch', 'source': 'host'},
        'holders': {'call': 'switch', 'source': 'holders'},
        'datacenters': {'call': 'fctDc',
                        'source': {**conn}},
        'active': {'call': 'setV', 'source': True},
        'accountant': {'call': 'fctAccountant', 'source': {**conn}},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}},
        'checksum': {'call': 'checksum',
                     'source': None}
    }
