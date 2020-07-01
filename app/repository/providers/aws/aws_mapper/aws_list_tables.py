def rules(conn):
    return {
        'name|unique_id|tables': {
            'call': 'tablesDynamoDB',
            'source': {
                'key': 'TableNames',
                'conn': conn
            },
            'merged': True
        },

        'created_at': {'call': 'now', 'source': 'createdDate'},
        'updated_at': {'call': 'now', 'source': 'createdDate'},

        'description': {'call': 'switch', 'source': 'description'},

        'provider': {'call': 'setV', 'source': 'DynamoDB (AWS)'},

        'family': {'call': 'setV', 'source': 'Database'},
        'active': {'call': 'setV', 'source': True},

        'datacenters': {'call': 'fctDcApp',
                        'source': {**conn}},
        'own': {'call': 'setV', 'source': 1},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'accountant': {'call': 'fctAccountant', 'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}},
        'checksum': {'call': 'checksum',
                     'source': None}
    }
