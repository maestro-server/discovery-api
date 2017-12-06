def rules(conn):
    return {
        'unique_id': {'call': 'switch', 'source': 'NetworkAclId'},
        'associations': {'call': 'switch', 'source': 'Associations'},
        'entries': {'call': 'switch', 'source': 'Entries'},
        'is_default': {'call': 'switch', 'source': 'IsDefault'},
        'vpc_id': {'call': 'switch', 'source': 'VpcId'},
        'family': {'call': 'setV', 'source': 'NetworkAcl'},
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