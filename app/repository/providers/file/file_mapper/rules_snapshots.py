def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'name'},
        'unique_id': {'call': 'switch', 'source': 'unique_id'},
        'volume_id': {'call': 'switch', 'source': 'volume_id'},
        'volume_size': {'call': 'switch', 'source': 'volume_size'},
        'status': {'call': 'switch', 'source': 'status'},

        'snapshot_id': {'call': 'switch', 'source': 'snapshot_id'},
        'size': {'call': 'switch', 'source': 'size'},

        'progress': {'call': 'switch', 'source': 'progress'},
        'tags': {'call': 'switch', 'source': 'tags'},
        'kms_key_id': {'call': 'switch', 'source': 'kms_key_id'},

        'encrypted': {'call': 'switch', 'source': 'encrypted'},

        'description': {'call': 'switch', 'source': 'description'},

        'project_id': {'call': 'switch', 'source': 'project_id'},
        'service': {'call': 'switch', 'source': 'service'},
        'data_encryption_key_id': {'call': 'switch', 'source': 'data_encryption_key_id'},

        'owner_id': {'call': 'switch', 'source': 'owner_id'},
        'start_time': {'call': 'switch', 'source': 'start_time'},
        'owner_alias': {'call': 'switch', 'source': 'owner_alias'},
        'state_message': {'call': 'switch', 'source': 'state_message'},
        'min_disk_size': {'call': 'switch', 'source': 'min_disk_size'},
        'public': {'call': 'switch', 'source': 'public'},

        'type': {'call': 'switch', 'source': 'type'},

        'active': {'call': 'setV', 'source': True},
        'datacenters': {'call': 'fctDc',
                        'source': {**conn}},

        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'accountant': {'call': 'fctAccountant', 'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}},
        'checksum': {'call': 'checksum',
                     'source': None}
    }
