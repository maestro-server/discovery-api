def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'name'},
        'service': {'call': 'switch', 'source': 'service'},
        'routes': {'call': 'switch', 'source': 'routes'},
        'allow_list': {'call': 'switch', 'source': 'allow_list'},
        'unique_id': {'call': 'switch', 'source': 'id'},
        'flavor_id': {'call': 'switch', 'source': 'flavor_id'},
        'external_gateway_info': {'call': 'switch', 'source': 'external_gateway_info'},
        'project_id': {'call': 'switch', 'source': 'project_id'},
        'availability_zone_hints': {'call': 'switch', 'source': 'availability_zone_hints'},
        'status': {'call': 'switch', 'source': 'status'},
        'description': {'call': 'switch', 'source': 'description'},
        'own': {'call': 'setV', 'source': 1},
        'family': {'call': 'setV', 'source': 'RouteTable'},
        'datacenters': {'call': 'fctDcApp',
                        'source': {**conn}},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'active': {'call': 'setV', 'source': True},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}}
    }
