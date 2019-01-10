def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'FunctionName'},
        'unique_id': {'call': 'switch', 'source': 'FunctionArn'},
        'created_at': {'call': 'switch', 'source': 'LastModified'},
        'updated_at': {'call': 'switch', 'source': 'LastModified'},
        'provider': {'call': 'setV', 'source': 'Lambda (AWS)'},
        'family': {'call': 'setV', 'source': 'Serverless'},
        'active': {'call': 'setV', 'source': True},

        'role': {'call': 'batch',
                 'source': {
                     'language': {'call': 'switch', 'source': 'Runtime'},
                     'aws_role': {'call': 'switch', 'source': 'Role'},
                     'handler': {'call': 'switch', 'source': 'Handler'},
                     'code_size': {'call': 'switch', 'source': 'CodeSize'},
                     'description': {'call': 'switch', 'source': 'Description'},
                     'timeout': {'call': 'switch', 'source': 'Timeout'},
                     'memory_size': {'call': 'switch', 'source': 'MemorySize'},
                     'code_sha_256': {'call': 'switch', 'source': 'CodeSha256'},
                     'vpc_config': {'call': 'switch', 'source': 'VpcConfig'},
                     'dead_letter_config': {'call': 'switch', 'source': 'DeadLetterConfig'},
                     'rnvironment': {'call': 'switch', 'source': 'Environment'},
                     'KMS_key_arn': {'call': 'switch', 'source': 'KMSKeyArn'},
                     'master_arn': {'call': 'switch', 'source': 'MasterArn'},
                     'tracing_config': {'call': 'switch', 'source': 'TracingConfig'},
                     'layers': {'call': 'switch', 'source': 'Layers'},
                     'tevision_id': {'call': 'switch', 'source': 'RevisionId'}
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
