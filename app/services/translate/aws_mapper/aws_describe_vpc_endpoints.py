def rules(conn):
    return {
        'unique_id': {'call': 'switch', 'source': 'VpcEndpointId'},
        'vpc_endpoint_type': {'call': 'switch', 'source': 'VpcEndpointType'},
        'vpc_id': {'call': 'switch', 'source': 'VpcId'},
        'service_name': {'call': 'switch', 'source': 'ServiceName'},
        'policy_document': {'call': 'switch', 'source': 'PolicyDocument'},
        'route_table_ids': {'call': 'switch', 'source': 'RouteTableIds'},
        'subnet_ids': {'call': 'switch', 'source': 'SubnetIds'},
        'groups': {'call': 'switch', 'source': 'Groups'},
        'private_dns_enabled': {'call': 'switch', 'source': 'PrivateDnsEnabled'},
        'network_interface_ids': {'call': 'switch', 'source': 'NetworkInterfaceIds'},
        'dns_entries': {'call': 'switch', 'source': 'DnsEntries'},
        'created_at': {'call': 'switch', 'source': 'CreationTimestamp'},

        'family': {'call': 'setV', 'source': 'VpcEndpoint'},
        'datacenters': {'call': 'fctDcApp',
                        'source': {**conn}},
        'environment': {'call': 'arrCatcher',
                        'source': {'field': 'Tags', 'sKey': 'Key', 's': 'environment', 'catcher': 'Value'}},
        'status': {'call': 'switch', 'source': 'State'},
        'tags': {'call': 'fctTags', 'source': 'Tags'},
        'active': {'call': 'switchOptions',
                   'source': {'field': 'State',
                              'options': {'Deleting': False, 'Deleted': False, 'Rejected': False, 'Failed': False, 'Expired': False},
                              'default': True
                              }},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}}
    }