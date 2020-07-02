def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'name'},
        'unique_id': {'call': 'switch', 'source': 'unique_id'},
        'iops': {'call': 'switch', 'source': 'iops'},
        'encrypted': {'call': 'switch', 'source': 'encrypted'},
        'size': {'call': 'switch', 'source': 'size'},

        'fftype': {'call': 'switch', 'source': 'fftype'},
        'kms_key_id': {'call': 'switch', 'source': 'kms_key_id'},
        'source_volume_id': {'call': 'switch', 'source': 'source_volume_id'},
        'storage_account_type': {'call': 'switch', 'source': 'storage_account_type'},
        'tags': {'call': 'switch', 'source': 'tags'},
        'write_accelerator_enabled': {'call': 'switch', 'source': 'write_accelerator_enabled'},
        'vhd': {'call': 'switch', 'source': 'vhd'},
        'diff_disk_settings': {'call': 'switch', 'source': 'diff_disk_settings'},
        'create_option': {'call': 'switch', 'source': 'create_option'},
        'sectors': {'call': 'switch', 'source': 'sectors'},
        'sectorsize': {'call': 'switch', 'source': 'sectorsize'},
        'support_discard': {'call': 'switch', 'source': 'support_discard'},

        'host': {'call': 'switch', 'source': 'host'},
        'holders': {'call': 'switch', 'source': 'holders'},
        'migration_id': {'call': 'switch', 'source': 'migration_id'},
        'image_id': {'call': 'switch', 'source': 'image_id'},
        'volume_type': {'call': 'switch', 'source': 'volume_type'},
        'snapshot_id': {'call': 'switch', 'source': 'snapshot_id'},

        'project_id': {'call': 'switch', 'source': 'project_id'},
        'service': {'call': 'switch', 'source': 'service'},
        'droplets_ids': {'call': 'switch', 'source': 'droplets_ids'},

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
