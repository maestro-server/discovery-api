def rules(conn):
    return {
        'unique_id': {'call': 'switch', 'source': 'SnapshotId'},
        'name': {'call': 'arrCatcher',
                 'source': {'field': 'Tags', 'sKey': 'Key', 's': 'name', 'catcher': 'Value'}},
        'data_encryption_key_id': {'call': 'switch', 'source': 'DataEncryptionKeyId'},
        'encrypted': {'call': 'switch', 'source': 'Encrypted'},
        'kms_key_id': {'call': 'switch', 'source': 'KmsKeyId'},
        'owner_id': {'call': 'switch', 'source': 'OwnerId'},
        'progress': {'call': 'switch', 'source': 'Progress'},
        'start_time': {'call': 'switch', 'source': 'StartTime'},
        'state_message': {'call': 'fctStorageImage', 'source': 'StateMessage'},
        'volume_id': {'call': 'switch', 'source': 'VolumeId'},
        'size': {'call': 'switch', 'source': 'VolumeSize'},
        'owner_alias': {'call': 'switch', 'source': 'OwnerAlias'},
        'datacenters': {'call': 'fctDcApp',
                        'source': {**conn}},
        'environment': {'call': 'arrCatcher',
                        'source': {'field': 'Tags', 'sKey': 'Key', 's': 'environment', 'catcher': 'Value'}},
        'status': {'call': 'switchCapitalized', 'source': 'State'},
        'active': {'call': 'switchOptions',
                   'source': {'field': 'State',
                              'options': {'error': False},
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