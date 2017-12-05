def rules(conn):
    return {
        'hostname': {'call': 'switch', 'source': 'name'},
        'unique_id': {'call': 'switch', 'source': 'id'},
        'ipv4_private': {'call': 'fctPrivateIp', 'source': 'addresses'},
        'ipv4_public': {'call': 'fctPublicIp', 'source': 'addresses'},
        'environment': {'call': 'switch', 'source': 'metadata.environment'},
        'role': {'call': 'switch', 'source': 'metadata.role'},
        'auth': {'call': 'fctAuth', 'source': 'key_name'},
        'storage': {'call': 'fctStorage', 'source': 'attached_volumes'},
        'created_at': {'call': 'switch', 'source': 'created_at'},
        'datacenters': {'call': 'fctDc',
                        'source': {**conn}},
        'meta': {'call': 'batch',
                 'source': {
                     'addresses': {'call': 'switch', 'source': 'addresses'},
                     'has_config_drive': {'call': 'switch', 'source': 'has_config_drive'},
                     'block_device_mapping': {'call': 'switch', 'source': 'block_device_mapping'}
                 }
                 },
        'tags': {'call': 'fctTags', 'source': 'metadata'},
        'status': {'call': 'switchOptions',
                   'source': {'field': 'status',
                              'options': {'REBOOT': 'Avaliable',
                                          'STOPPED': 'Stopped',
                                          'SHUTOFF': 'Stopped',
                                          'SUSPENDED': 'Stopped',
                                          'PAUSED': 'Stopped'},
                              'default': 'Active'
                              }},
        'active': {'call': 'switchOptions',
                   'source': {'field': 'status',
                              'options': {'DELETED': False,
                                          'ERROR': False,
                                          'SOFT_DELETED': False,
                                          'UNKNOWN': False},
                              'default': True
                              }},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}}
    }
