def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'name'},
        'unique_id': {'call': 'switch', 'source': 'id'},

        'role': {'call': 'batch',
                 'source': {
                     'ip': {'call': 'switch', 'source': 'ip'},
                     'algorithm': {'call': 'switch', 'source': 'algorithm'},
                     'forwarding_rules': {'call': 'switch', 'source': 'forwarding_rules'},
                     'health_check': {'call': 'switch', 'source': 'health_check'},
                     'sticky_sessions': {'call': 'switch', 'source': 'sticky_sessions'},
                     'droplet_ids': {'call': 'switch', 'source': 'droplet_ids'},
                     'redirect_http_to_https': {'call': 'switch', 'source': 'redirect_http_to_https'}
                 }
                 },

        'datacenters': {'call': 'fctDc',
                        'source': {**conn}},

        'created_at': {'call': 'switch', 'source': 'created_at'},
        'updated_at': {'call': 'switch', 'source': 'created_at'},

        'status': {'call': 'switchCapitalized', 'source': 'status'},
        'active': {'call': 'switchOptions',
                   'source': {'field': 'status',
                              'options': {
                                  "errored": False
                              },
                              'default': True
                              }},
        'provider': {'call': 'setV', 'source': 'LB (DigitalOcean)'},
        'own': {'call': 'setV', 'source': 1},
        'family': {'call': 'setV', 'source': 'Loadbalance'},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'accountant': {'call': 'fctAccountant', 'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}},
        'checksum': {'call': 'checksum',
                     'source': None}
    }
