def rules(conn):
    return {
        'hostname': {'call': 'arrCatcher',
                     'source': {'field': 'Tags', 'sKey': 'Key', 's': 'name', 'catcher': 'Value'}},
        'unique_id': {'call': 'switch', 'source': 'InstanceId'},
        'role': {'call': 'arrCatcher',
                 'source': {'field': 'Tags', 'sKey': 'Key', 's': 'role', 'catcher': 'Value'}},
        'environment': {'call': 'arrCatcher',
                        'source': {'field': 'Tags', 'sKey': 'Key', 's': 'environment', 'catcher': 'Value'}},
        'created_at': {'call': 'switch', 'source': 'LaunchTime'},
        'ipv4_private': {'call': 'switch', 'source': 'PrivateIpAddress'},
        'ipv4_public': {'call': 'switch', 'source': 'PublicIpAddress'},
        'dns_public': {'call': 'switch', 'source': 'PublicDnsName'},
        'dns_private': {'call': 'switch', 'source': 'PrivateDnsName'},
        'storage': {'call': 'fctStorage', 'source': 'BlockDeviceMappings'},
        'auth': {'call': 'fctAuth', 'source': 'KeyName'},
        'tags': {'call': 'fctTags', 'source': 'Tags'},
        'ebs_optimized': {'call': 'switch', 'source': 'EbsOptimized'},
        'status': {'call': 'switchOptions',
                   'source': {'field': 'State.Name',
                              'options': {'running': 'Active', 'pending': 'Active', 'stopping': 'Stopped',
                                          'stopped': 'Stopped'},
                              'default': None
                              }},
        'active': {'call': 'switchOptions',
                   'source': {'field': 'State.Name',
                              'options': {'shutting-down': False, 'terminated': False},
                              'default': True
                              }},
        'metas': {'call': 'batch',
                 'source': {
                     'security_groups': {'call': 'switch', 'source': 'SecurityGroups'},
                     'iam_instance_profile': {'call': 'switch', 'source': 'IamInstanceProfile'}
                 }
                 },
        'datacenters': {'call': 'fctDc',
                        'source': {**conn}},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}}
    }
