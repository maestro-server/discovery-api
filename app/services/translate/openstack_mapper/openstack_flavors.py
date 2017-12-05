def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'name'},
        'unique_id': {'call': 'switch', 'source': 'id'},
        'ram': {'call': 'switch', 'source': 'ram'},
        'disk': {'call': 'switch', 'source': 'disk'},
        'vcpus': {'call': 'switch', 'source': 'vcpus'},
        'is_public': {'call': 'switch', 'source': 'is_public'},
        'service': {'call': 'switch', 'source': 'service'},
        'ephemeral': {'call': 'switch', 'source': 'ephemeral'},
        'datacenters': {'call': 'fctDcApp',
                        'source': {**conn}},
        'own': {'call': 'setV', 'source': 1},
        'active': {'call': 'setV', 'source': True},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}}
    }
