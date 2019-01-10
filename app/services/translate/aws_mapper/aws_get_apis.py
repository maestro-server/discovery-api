def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'Name'},
        'unique_id': {'call': 'switch', 'source': 'ApiId'},

        'created_at': {'call': 'switch', 'source': 'CreatedDate'},
        'updated_at': {'call': 'switch', 'source': 'CreatedDate'},

        'description': {'call': 'switch', 'source': 'Description'},

        'provider': {'call': 'setV', 'source': 'ApiGateway (AWS)'},

        'family': {'call': 'setV', 'source': 'ApiGateway'},
        'active': {'call': 'setV', 'source': True},

        'role': {'call': 'batch',
                 'source': {
                     'ApiKeySelection_expression': {'call': 'switch', 'source': 'ApiKeySelectionExpression '},
                     'disable_schema_validation': {'call': 'switch', 'source': 'DisableSchemaValidation'},
                     'endpoint': {'call': 'switch', 'source': 'ApiEndpoint'},
                     'protocol_type': {'call': 'switch', 'source': 'ProtocolType'},
                     'route_selection_expression': {'call': 'switch', 'source': 'RouteSelectionExpression'},
                     'version': {'call': 'switch', 'source': 'Version'},
                     'warnings': {'call': 'switch', 'source': 'Warnings'}
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
