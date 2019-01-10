def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'name'},
        'unique_id': {'call': 'switch', 'source': 'id'},

        'created_at': {'call': 'switch', 'source': 'createdDate'},
        'updated_at': {'call': 'switch', 'source': 'createdDate'},

        'description': {'call': 'switch', 'source': 'description'},

        'provider': {'call': 'setV', 'source': 'ApiGateway (AWS)'},

        'family': {'call': 'setV', 'source': 'ApiGateway'},
        'active': {'call': 'setV', 'source': True},

        'role': {'call': 'batch',
                 'source': {
                     'version': {'call': 'switch', 'source': 'version'},
                     'warnings': {'call': 'switch', 'source': 'warnings'},
                     'binary_media_types': {'call': 'switch', 'source': 'binaryMediaTypes'},
                     'minimum_compression_size': {'call': 'switch', 'source': 'minimumCompressionSize'},
                     'api_key_source': {'call': 'switch', 'source': 'apiKeySource'},
                     'endpoint_configuration': {'call': 'switch', 'source': 'endpointConfiguration'},
                     'policy': {'call': 'switch', 'source': 'policy'}
                 }
         },

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
