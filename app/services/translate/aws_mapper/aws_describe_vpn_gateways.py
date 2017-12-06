def rules(conn):
    return {
        'unique_id': {'call': 'switch', 'source': 'VpnGatewayId'},
        'availability_zone': {'call': 'switch', 'source': 'AvailabilityZone'},
        'vpc_attachments': {'call': 'switch', 'source': 'VpcAttachments'},
        'amazon_side_asn': {'call': 'switch', 'source': 'AmazonSideAsn'},
        'family': {'call': 'setV', 'source': 'VpnGateways'},
        'datacenters': {'call': 'fctDcApp',
                        'source': {**conn}},
        'environment': {'call': 'arrCatcher',
                        'source': {'field': 'Tags', 'sKey': 'Key', 's': 'environment', 'catcher': 'Value'}},
        'status': {'call': 'switch', 'source': 'State'},
        'tags': {'call': 'fctTags', 'source': 'Tags'},
        'active': {'call': 'switchOptions',
                   'source': {'field': 'State',
                              'options': {'deleted': False, 'deleting': False},
                              'default': True
                              }},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}}
    }