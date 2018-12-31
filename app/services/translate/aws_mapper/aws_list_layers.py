def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'LayerVersionArn'},
        'unique_id': {'call': 'switch', 'source': 'LayerVersionArn'},
        'created_at': {'call': 'switch', 'source': 'CreationDate'},
        'updated_at': {'call': 'switch', 'source': 'CreationDate'},
        'provider': {'call': 'setV', 'source': 'AWS Lambda Layer'},

        'family': {'call': 'setV', 'source': 'ServerlessLayer'},
        'Description': {'call': 'setV', 'source': 'Description'},
        'runtimes': {'call': 'setV', 'source': 'CompatibleRuntimes'},
        'license_info': {'call': 'setV', 'source': 'LicenseInfo'},
        'version': {'call': 'setV', 'source': 'Version'},

        'active': {'call': 'setV', 'source': True},
        'datacenters': {'call': 'fctDcApp',
                        'source': {**conn}},
        'own': {'call': 'setV', 'source': 1},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}},
        'checksum': {'call': 'checksum',
                     'source': None}
    }
