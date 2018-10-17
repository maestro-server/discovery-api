def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'DomainName'},
        'origins': {'call': 'switch', 'source': 'Origins'},
        'cache_behavior': {'call': 'switch', 'source': 'CacheBehaviors'},
        'unique_id': {'call': 'switch', 'source': 'Id'},
        'status': {'call': 'switch', 'source': 'Status'},
        'datacenters': {'call': 'fctDcApp',
                        'source': {**conn}},
        'active': {'call': 'switchOptions',
                   'source': {'field': 'Status',
                              'options': {'failed': False, 'active_impaired': False, 'deleting': False},
                              'default': True
                              }},
        'environment': {'call': 'arrCatcher',
                        'source': {'field': 'Tags', 'sKey': 'Key', 's': 'environment', 'catcher': 'Value'}},
        'created_at': {'call': 'switch', 'source': 'CreatedTime'},
        'updated_at': {'call': 'switch', 'source': 'CreatedTime'},
        'provider': {'call': 'setV', 'source': 'CloudFront (AWS)'},
        'own': {'call': 'setV', 'source': 1},
        'tags': {'call': 'fctTags', 'source': 'Tags'},
        'family': {'call': 'setV', 'source': 'CDN'},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}},
        'checksum': {'call': 'checksum',
                     'source': None}
    }
