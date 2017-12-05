def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'name'},
        'unique_id': {'call': 'switch', 'source': 'id'},
        'source_volume_id': {'call': 'switch', 'source': 'source_volume_id'},
        'migration_id': {'call': 'switch', 'source': 'migration_id'},
        'image_id': {'call': 'switch', 'source': 'image_id'},
        'status': {'call': 'switch', 'source': 'status'},
        'encrypted': {'call': 'switch', 'source': 'is_encrypted'},
        'description': {'call': 'switch', 'source': 'description'},
        'volume_type': {'call': 'switch', 'source': 'volume_type'},
        'snapshot_id': {'call': 'switch', 'source': 'snapshot_id'},
        'project_id': {'call': 'switch', 'source': 'project_id'},
        'size': {'call': 'switch', 'source': 'size'},
        'service': {'call': 'switch', 'source': 'service'},
        'datacenters': {'call': 'fctDcApp',
                        'source': {**conn}},
        'own': {'call': 'setV', 'source': 1},
        'active': {'call': 'setV', 'source': True},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}}
    }
