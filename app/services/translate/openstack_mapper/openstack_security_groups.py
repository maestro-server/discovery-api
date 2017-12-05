def rules(conn):
    return {
        'unique_id': {'call': 'switch', 'source': 'id'},
        'ip_permissions': {'call': 'switch', 'source': 'security_group_rules'},
        'resource_key': {'call': 'switch', 'source': 'resource_key'},
        'service': {'call': 'switch', 'source': 'service'},
        'project_id': {'call': 'switch', 'source': 'project_id'},
        'name': {'call': 'switch', 'source': 'name'},
        'own': {'call': 'setV', 'source': 1},
        'family': {'call': 'setV', 'source': 'SecurityGroup'},
        'datacenters': {'call': 'fctDc',
                        'source': {**conn}},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'active': {'call': 'setV', 'source': True},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}}
    }
