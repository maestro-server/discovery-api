def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'DomainName'},
        'unique_id': {'call': 'switch', 'source': 'Id'},

        'role': {'call': 'batch',
                 'source': {
                     's3_origin': {'call': 'switch', 'source': 'S3Origin'},
                     'trusted_signers': {'call': 'switch', 'source': 'TrustedSigners'},
                     'Aliases': {'call': 'switch', 'source': 'Aliases.Items'},
                     'price_class': {'call': 'switch', 'source': 'PriceClass'},
                     'enabled': {'call': 'switch', 'source': 'Enabled'}
                 }
                 },


        'status': {'call': 'switchCapitalized', 'source': 'Status'},
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
        'type': {'call': 'setV', 'source': 'RTMP'},
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
