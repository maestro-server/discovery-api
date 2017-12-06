def rules(conn):
    return {
        'unique_id': {'call': 'switch', 'source': 'NatGatewayId'},
        'vpc_id': {'call': 'switch', 'source': 'VpcId'},
        'subnet_id': {'call': 'switch', 'source': 'SubnetId'},
        'provisioned_bandwidth': {'call': 'switch', 'source': 'ProvisionedBandwidth'},
        'nat_gateway_addresses': {'call': 'switch', 'source': 'NatGatewayAddresses'},
        'failure_code': {'call': 'switch', 'source': 'FailureCode'},
        'failure_message': {'call': 'switch', 'source': 'FailureMessage'},
        'delete_time': {'call': 'switch', 'source': 'DeleteTime'},
        'created_at': {'call': 'switch', 'source': 'CreateTime'},
        'family': {'call': 'setV', 'source': 'NatGateway'},
        'datacenters': {'call': 'fctDcApp',
                        'source': {**conn}},
        'environment': {'call': 'arrCatcher',
                        'source': {'field': 'Tags', 'sKey': 'Key', 's': 'environment', 'catcher': 'Value'}},
        'status': {'call': 'switch', 'source': 'State'},
        'tags': {'call': 'fctTags', 'source': 'Tags'},
        'active': {'call': 'switchOptions',
                   'source': {'field': 'State',
                              'options': {'failed': False, 'deleting': False, 'deleted': False},
                              'default': True
                              }},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}}
    }