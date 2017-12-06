def rules(conn):
    return {
        'unique_id': {'call': 'switch', 'source': 'VpcId'},
        'name': {'call': 'arrCatcher',
                     'source': {'field': 'Tags', 'sKey': 'Key', 's': 'name', 'catcher': 'Value'}},
        'image_id': {'call': 'switch', 'source': 'CidrBlock'},
        'dhcp_options_id': {'call': 'switch', 'source': 'DhcpOptionsId'},
        'instance_tenancy': {'call': 'switch', 'source': 'InstanceTenancy'},
        'ipv6_cidr_block_association_set': {'call': 'switch', 'source': 'Ipv6CidrBlockAssociationSet'},
        'cidr_block_association_set': {'call': 'switch', 'source': 'CidrBlockAssociationSet'},
        'is_default': {'call': 'switch', 'source': 'IsDefault'},
        'family': {'call': 'setV', 'source': 'Vpc'},
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