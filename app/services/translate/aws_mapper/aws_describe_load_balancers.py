def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'LoadBalancerName'},
        'role': {'call': 'batch',
                 'source': {
                     'endpoint': {'call': 'switch', 'source': 'DNSName'},
                     'arn': {'call': 'switch', 'source': 'LoadBalancerArn'},
                     'canonical_hosted_zone': {'call': 'switch', 'source': 'CanonicalHostedZoneId'},
                     'vpc_id': {'call': 'switch', 'source': 'VpcId'},
                     'type': {'call': 'switch', 'source': 'Type'},
                     'ip_address_type': {'call': 'switch', 'source': 'IpAddressType'},
                     'backend_server_descriptions': {'call': 'switch', 'source': 'BackendServerDescriptions'},
                     'health_check_classic': {'call': 'switch', 'source': 'HealthCheck'},
                     'healthcheck': {'call': 'switch', 'source': 'HealthCheck.Target'},
                     'canonical_hosted_zone_name': {'call': 'switch', 'source': 'CanonicalHostedZoneName'},
                     'canonical_hosted_zone_name_id': {'call': 'switch', 'source': 'CanonicalHostedZoneNameID'}
                 }
                 },
        'datacenters': {'call': 'fctDcApp',
                        'source': {**conn}},
        'status': {'call': 'switch', 'source': 'State.Code'},
        'active': {'call': 'switchOptions',
                   'source': {'field': 'State.Code',
                              'options': {'failed': False, 'active_impaired': False},
                              'default': True
                              }},
        'environment': {'call': 'arrCatcher',
                        'source': {'field': 'Tags', 'sKey': 'Key', 's': 'environment', 'catcher': 'Value'}},
        'created_at': {'call': 'switch', 'source': 'CreatedTime'},
        'provider': {'call': 'setV', 'source': 'ELB (AWS)'},
        'own': {'call': 'setV', 'source': 1},
        'tags': {'call': 'fctTags', 'source': 'Tags'},
        'family': {'call': 'setV', 'source': 'Loadbalance'},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}}
    }
