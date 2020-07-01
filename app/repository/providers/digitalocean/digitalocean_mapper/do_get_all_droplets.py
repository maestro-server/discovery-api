def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'name'},
        'unique_id': {'call': 'switch', 'source': 'id'},
        'cpu': {'call': 'switch', 'source': 'vcpus'},
        'memory': {'call': 'getMemory', 'source': 'memory'},

        'image': {'call': 'switch', 'source': 'image'},
        'backup_ids': {'call': 'switch', 'source': 'backup_ids'},
        'next_backup_window': {'call': 'switch', 'source': 'next_backup_window'},
        'snapshot_ids': {'call': 'switch', 'source': 'snapshot_ids'},

        'ipv4_private': {'call': 'fctPrivateIp', 'source': 'networks.v4'},
        'ipv4_public': {'call': 'fctPublicIp', 'source': 'networks.v4'},

        'storage': {'call': 'fctStorage', 'source': 'volume_ids'},

        'datacenters': {'call': 'fctDc',
                        'source': {**conn}},

        'created_at': {'call': 'switch', 'source': 'created_at'},
        'updated_at': {'call': 'switch', 'source': 'created_at'},

        'active': {'call': 'switchOptions',
                   'source': {'field': 'status',
                              'options': {
                                  "off": False,
                                  "archive": False},
                              'default': True
                              }},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'accountant': {'call': 'fctAccountant', 'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}},
        'checksum': {'call': 'checksum',
                     'source': None}
    }
