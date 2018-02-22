def rules(conn):
    return {
        'unique_id': {'call': 'switch', 'source': 'VolumeId'},
        'name': {'call': 'arrCatcher',
                     'source': {'field': 'Tags', 'sKey': 'Key', 's': 'name', 'catcher': 'Value'}},
        'datacenters': {'call': 'fctDcApp',
                        'source': {**conn}},
        'environment': {'call': 'arrCatcher',
                        'source': {'field': 'Tags', 'sKey': 'Key', 's': 'environment', 'catcher': 'Value'}},
        'availability_zone': {'call': 'switch', 'source': 'AvailabilityZone'},
        'encrypted': {'call': 'switch', 'source': 'Encrypted'},
        'kms_key_id': {'call': 'switch', 'source': 'KmsKeyId'},
        'size': {'call': 'switch', 'source': 'Size'},
        'snapshot_id': {'call': 'switch', 'source': 'SnapshotId'},
        'iops': {'call': 'switch', 'source': 'Iops'},
        'status': {'call': 'switchOptions',
                   'source': {'field': 'State',
                              'options': {'creating': 'Active', 'available': 'Active', 'in-use': 'Active',
                                          'deleting': 'Deleted', 'deleted': 'Deleted', 'error': 'Error'},
                              'default': None
                              }},
        'active': {'call': 'switchOptions',
                   'source': {'field': 'State',
                              'options': {'deleting': False, 'deleted': False, 'error': False},
                              'default': True
                              }},
        'created_at': {'call': 'switch', 'source': 'CreatedTime'},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}}
    }