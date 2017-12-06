def rules(conn):
    return {
        'unique_id': {'call': 'switch', 'source': 'VpcPeeringConnectionId'},
        'accepter_vpc_info': {'call': 'switch', 'source': 'AccepterVpcInfo'},
        'expiration_time': {'call': 'switch', 'source': 'ExpirationTime'},
        'requester_vpc_info': {'call': 'switch', 'source': 'RequesterVpcInfo'},
        'family': {'call': 'setV', 'source': 'VpcPeering'},
        'datacenters': {'call': 'fctDcApp',
                        'source': {**conn}},
        'environment': {'call': 'arrCatcher',
                        'source': {'field': 'Tags', 'sKey': 'Key', 's': 'environment', 'catcher': 'Value'}},
        'tags': {'call': 'fctTags', 'source': 'Tags'},
        'status': {'call': 'switch', 'source': 'State'},
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