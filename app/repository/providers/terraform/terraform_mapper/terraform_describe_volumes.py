def rules(conn):
    return {
        'unique_id': {'call': 'switch',
                      'source': 'volume_id'},
        'size': {'call': 'switch',
                      'source': 'volume_size'},
        'iops': {'call': 'switch',
                      'source': 'iops'},
        'volume_type': {'call': 'switch',
                      'source': 'volume_type'},
        'encrypted': {'call': 'switch',
                      'source': 'encrypted'},
        'delete_on_termination': {'call': 'switch',
                      'source': 'delete_on_termination'},
        'kms_key_id': {'call': 'switch',
                      'source': 'kms_key_id'},


        'datacenters': {'call': 'fctDc',
                        'source': {**conn}},
        'active': {'call': 'setV', 'source': True},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'accountant': {'call': 'fctAccountant', 'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}},
        'checksum': {'call': 'checksum',
                     'source': None}
    }
