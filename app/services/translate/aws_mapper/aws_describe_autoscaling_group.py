def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'AutoScalingGroupName'},
        'unique_id': {'call': 'switch', 'source': 'AutoScalingGroupARN'},

        'loadbalance_names': {'call': 'switch', 'source': 'LoadBalancerNames'},
        'instances': {'call': 'switch', 'source': 'Instances'},

        'role': {'call': 'batch',
                 'source': {
                     'launch_configuration_name': {'call': 'switch', 'source': 'LaunchConfigurationName'},
                     'launch_template': {'call': 'switch', 'source': 'LaunchTemplate'},
                     'min_size': {'call': 'switch', 'source': 'MinSize'},
                     'max_size': {'call': 'switch', 'source': 'MaxSize'},
                     'desired_capacity': {'call': 'switch', 'source': 'DesiredCapacity'},
                     'health_check_type': {'call': 'switch', 'source': 'HealthCheckType'},
                     'health_check_grace_period': {'call': 'switch', 'source': 'HealthCheckGracePeriod'},
                     'default_cooldown': {'call': 'switch', 'source': 'DefaultCooldown'},
                     'vpc_zone_identifier': {'call': 'switch', 'source': 'VPCZoneIdentifier'},
                 }
                 },
        'status': {'call': 'switch', 'source': 'Status'},

        'datacenters': {'call': 'fctDcApp',
                        'source': {**conn}},
        'active': {'call': 'setV', 'source': True},

        'environment': {'call': 'arrCatcher',
                        'source': {'field': 'Tags', 'sKey': 'Key', 's': 'environment', 'catcher': 'Value'}},
        'created_at': {'call': 'switch', 'source': 'CreatedTime'},
        'provider': {'call': 'setV', 'source': 'AutoScaling (AWS)'},
        'own': {'call': 'setV', 'source': 1},
        'tags': {'call': 'fctTags', 'source': 'Tags'},
        'family': {'call': 'setV', 'source': 'AutoScaling'},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}},
        'checksum': {'call': 'checksum',
                     'source': None}
    }
