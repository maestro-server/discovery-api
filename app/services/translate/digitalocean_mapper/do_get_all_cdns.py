def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'endpoint'},
        'unique_id': {'call': 'switch', 'source': 'id'},

        'role': {'call': 'batch',
                 'source': {
                     'origins': {'call': 'switch', 'source': 'origin'},
                     'endpoint': {'call': 'switch', 'source': 'endpoint'},
                     'ttl': {'call': 'switch', 'source': 'ttl'}
                 }
                 },

        'datacenters': {'call': 'fctDc',
                        'source': {**conn}},

        'created_at': {'call': 'switch', 'source': 'created_at'},
        'updated_at': {'call': 'switch', 'source': 'created_at'},

        'active': {'call': 'switchOptions',
                   'source': {'field': 'status',
                              'options': {
                                  "deleted": False},
                              'default': True
                              }},

        'type': {'call': 'setV', 'source': 'Web'},
        'provider': {'call': 'setV', 'source': 'CDN (DigitalOcean)'},
        'own': {'call': 'setV', 'source': 1},
        'family': {'call': 'setV', 'source': 'CDN'},

        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}},
        'checksum': {'call': 'checksum',
                     'source': None}
    }
