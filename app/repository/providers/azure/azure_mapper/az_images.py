def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'name'},
        'unique_id': {'call': 'createID', 'source': {
            'key': 'id',
            'reg': r'^\/subscriptions/(.*)/resourceGroups/(.*)/providers/Microsoft.Compute/images/(.*)?'
        }},

        'datacenters': {'call': 'fctDc',
                        'source': {**conn}},

        'created_at': {'call': 'switch', 'source': 'time_created'},
        'updated_at': {'call': 'switch', 'source': 'time_created'},

        'environment': {'call': 'switch', 'source': 'tags.environment'},

        'tags': {'call': 'fctTags', 'source': 'tags'},
        'size': {'call': 'switch', 'source': 'disk_size_gb'},
        'encryption_settings': {'call': 'switch', 'source': 'encryption_settings'},
        'disk_iops_read_write': {'call': 'switch', 'source': 'disk_iops_read_write'},
        'disk_mbps_read_write': {'call': 'switch', 'source': 'disk_mbps_read_write'},
        'type': {'call': 'switch', 'source': 'type'},
        'managed_by': {'call': 'switch', 'source': 'managed_by'},
        'os_type': {'call': 'switch', 'source': 'os_type'},

        'status': {'call': 'switchOptions',
                   'source': {'field': 'provisioning_state',
                              'options': {
                                  "Succeeded": "Active"
                              },
                              'default': "Avaliable"
                              }},

        'active': {'call': 'setV', 'source': True},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'accountant': {'call': 'fctAccountant', 'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}},
        'checksum': {'call': 'checksum',
                     'source': None}
    }
