def rules(conn):
    return {
        'name|unique_id|domain': {
            'call': 'IdentitySES',
            'source': {
                'key': 'Identities',
                'conn': conn
            },
            'merged': True
        },

        'provider': {'call': 'setV', 'source': 'SES (AWS)'},
        'family': {'call': 'setV', 'source': 'SMTP'},
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
