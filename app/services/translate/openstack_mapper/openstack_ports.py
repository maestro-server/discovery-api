def rules(conn):
    return {
        'unique_id': {'call': 'switch', 'source': 'id'},
        'network_id': {'call': 'switch', 'source': 'network_id'},
        'description': {'call': 'switch', 'source': 'description'},
        'mac_address': {'call': 'switch', 'source': 'mac_address'},
        'service': {'call': 'switch', 'source': 'service'},
        'status': {'call': 'switch', 'source': 'status'},
        'project_id': {'call': 'switch', 'source': 'project_id'},
        'fixed_ips': {'call': 'switch', 'source': 'fixed_ips'},
        'subnet_ids': {'call': 'switch', 'source': 'subnet_ids'},
        'resources_key': {'call': 'switch', 'source': 'resources_key'},
        'device_id': {'call': 'switch', 'source': 'device_id'},
        'security_group_ids': {'call': 'switch', 'source': 'security_group_ids'},
        'own': {'call': 'setV', 'source': 1},
        'family': {'call': 'setV', 'source': 'Ports'},
        'datacenters': {'call': 'fctDcApp',
                        'source': {**conn}},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'active': {'call': 'setV', 'source': True},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}}
    }
