def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'name'},
        'api_name': {'call': 'switch', 'source': 'name'},
        'unique_id': {'call': 'switch', 'source': 'id'},
        'memory': {'call': 'switch', 'source': 'ram'},
        'disk': {'call': 'switch', 'source': 'disk'},
        'vcpus': {'call': 'switch', 'source': 'vcpus'},
        'is_public': {'call': 'switch', 'source': 'is_public'},
        'service': {'call': 'switch', 'source': 'service'},
        'ephemeral': {'call': 'switch', 'source': 'ephemeral'},
        'provider': {'call': 'setV', 'source': 'OpenStack'},
        'datacenters': {'call': 'fctDcApp',
                        'source': {**conn}},
        'active': {'call': 'setV', 'source': True},
    }
