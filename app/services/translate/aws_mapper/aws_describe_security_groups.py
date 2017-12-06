def rules(conn):
    return {
        'unique_id': {'call': 'switch', 'source': 'GroupId'},
        'name': {'call': 'switch', 'source': 'GroupName'},
        'group_name': {'call': 'switch', 'source': 'GroupName'},
        'description': {'call': 'switch', 'source': 'Description'},
        'ip_permissions': {'call': 'switch', 'source': 'IpPermissions'},
        'vpc_id': {'call': 'switch', 'source': 'VpcId'},
        'family': {'call': 'setV', 'source': 'SecurityGroup'},
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