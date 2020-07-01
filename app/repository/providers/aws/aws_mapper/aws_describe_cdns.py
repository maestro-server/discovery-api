def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'DomainName'},
        'origins': {'call': 'switch', 'source': 'Origins'},
        'cache_behavior': {'call': 'switch', 'source': 'CacheBehaviors'},
        'unique_id': {'call': 'switch', 'source': 'Id'},

        'role': {'call': 'batch',
                 'source': {
                     'origins': {'call': 'switch', 'source': 'Origins.Items'},
                     'default_cache_behavior': {'call': 'switch', 'source': 'DefaultCacheBehavior'},
                     'cache_behaviors': {'call': 'switch', 'source': 'CacheBehaviors.Items'},
                     'custom_error': {'call': 'switch', 'source': 'CustomErrorResponses.Items'},
                     'restrictions': {'call': 'switch', 'source': 'Restrictions'},
                     'web_acl_id': {'call': 'switch', 'source': 'WebACLId'},
                     'http_version': {'call': 'switch', 'source': 'HttpVersion'},
                     'ipv6_enabled': {'call': 'switch', 'source': 'IsIPV6Enabled'}
                 }
                 },


        'status': {'call': 'switchCapitalized', 'source': 'Status'},
        'state': {'call': 'switch', 'source': 'Enabled'},
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
        'type': {'call': 'setV', 'source': 'Web'},
        'provider': {'call': 'setV', 'source': 'CloudFront (AWS)'},
        'own': {'call': 'setV', 'source': 1},
        'tags': {'call': 'fctTags', 'source': 'Tags'},
        'family': {'call': 'setV', 'source': 'CDN'},
        'accountant': {'call': 'fctAccountant', 'source': {**conn}},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}},
        'checksum': {'call': 'checksum',
                     'source': None}
    }
