def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'name|id'},
        'unique_id': {'call': 'switch', 'source': 'id'},
        'source_volume_id': {'call': 'switch', 'source': 'source_volume_id'},
        'migration_id': {'call': 'switch', 'source': 'migration_id'},
        'image_id': {'call': 'switch', 'source': 'image_id'},
        'image_name': {'call': 'switch', 'source': 'image_name'},
        'container_format': {'call': 'switch', 'source': 'container_format'},
        'encrypted': {'call': 'switch', 'source': 'is_encrypted'},
        'description': {'call': 'switch', 'source': 'description'},
        'volume_type': {'call': 'switch', 'source': 'volume_type'},
        'snapshot_id': {'call': 'switch', 'source': 'snapshot_id'},
        'project_id': {'call': 'switch', 'source': 'project_id'},
        'size': {'call': 'switch', 'source': 'size'},
        'service': {'call': 'switch', 'source': 'service'},
        'created_at': {'call': 'switch', 'source': 'created_at'},
        'updated_at': {'call': 'switch', 'source': 'created_at'},
        'status': {'call': 'switchOptions',
                   'source': {'field': 'status',
                              'options': {'creating': 'Active', 'available': 'Available', 'in-use': 'Active',
                                          'deleting': 'Deleted', 'deleted': 'Deleted', 'error': 'Error'},
                              'default': None
                              }},
        'datacenters': {'call': 'fctDcApp',
                        'source': {**conn}},
        'own': {'call': 'setV', 'source': 1},
        'active': {'call': 'setV', 'source': True},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'accountant': {'call': 'fctAccountant', 'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}},
        'checksum': {'call': 'checksum',
                     'source': None}
    }