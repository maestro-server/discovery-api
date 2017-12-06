def rules(conn):
    return {
        'unique_id': {'call': 'switch', 'source': 'SubnetId'},
        'availability_zone': {'call': 'switch', 'source': 'AvailabilityZone'},
        'available_ip_address_count': {'call': 'switch', 'source': 'AvailableIpAddressCount'},
        'cidr_block': {'call': 'switch', 'source': 'CidrBlock'},
        'default_for_az': {'call': 'switch', 'source': 'DefaultForAz'},
        'map_public_ip_on_launch': {'call': 'switch', 'source': 'MapPublicIpOnLaunch'},
        'vpc_id': {'call': 'switch', 'source': 'VpcId'},
        'assign_ipv6_address_on_creation': {'call': 'switch', 'source': 'AssignIpv6AddressOnCreation'},
        'ipv6Cidr_block_association_set': {'call': 'switch', 'source': 'Ipv6CidrBlockAssociationSet'},
        'family': {'call': 'setV', 'source': 'Subnet'},
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