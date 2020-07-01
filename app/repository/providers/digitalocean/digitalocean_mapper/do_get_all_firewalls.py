def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'name'},
        'unique_id': {'call': 'switch', 'source': 'id'},

        'inbound_rules': {'call': 'switch', 'source': 'inbound_rules'},
        'outbound_rules': {'call': 'switch', 'source': 'outbound_rules'},

        'pending_changes': {'call': 'switch', 'source': 'pending_changes'},
        'droplet_ids': {'call': 'switch', 'source': 'droplet_ids'},

        'datacenters': {'call': 'fctDc',
                        'source': {**conn}},

        'created_at': {'call': 'switch', 'source': 'created_at'},
        'updated_at': {'call': 'switch', 'source': 'created_at'},

        'family': {'call': 'setV', 'source': 'Firewall'},
        'status': {'call': 'switchCapitalized', 'source': 'status'},
        'active': {'call': 'switchOptions',
                   'source': {'field': 'status',
                              'options': {
                                  "failed": False},
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
