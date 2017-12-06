def rules(conn):
    return {
        'unique_id': {'call': 'switch', 'source': 'RouteTableId'},
        'associations': {'call': 'switch', 'source': 'Associations'},
        'propagating_vgws': {'call': 'switch', 'source': 'PropagatingVgws'},
        'routes': {'call': 'switch', 'source': 'Routes'},
        'vpc_id': {'call': 'switch', 'source': 'VpcId'},
        'family': {'call': 'setV', 'source': 'RouteTable'},
        'datacenters': {'call': 'fctDcApp',
                        'source': {**conn}},
        'environment': {'call': 'arrCatcher',
                        'source': {'field': 'Tags', 'sKey': 'Key', 's': 'environment', 'catcher': 'Value'}},
        'status': {'call': 'switch', 'source': 'State'},
        'tags': {'call': 'fctTags', 'source': 'Tags'},
        'active': {'call': 'switchOptions',
                   'source': {'field': 'State',
                              'options': {'error': False, 'invalid': False},
                              'default': True
                              }},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}}
    }