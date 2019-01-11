def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'DomainName'},
        'unique_id': {'call': 'switch', 'source': 'DomainId'},

        'created_at': {'call': '', 'source': 'Created'},
        'updated_at': {'call': 'now', 'source': 'Created'},

        'provider': {'call': 'setV', 'source': 'CloudSearch (AWS)'},
        'family': {'call': 'setV', 'source': 'Database'},
        'engine': {'call': 'setV', 'source': 'CloudSearch'},
        'active': {'call': 'setV', 'source': True},

        'role': {'call': 'batch',
                 'source': {
                     'arn': {'call': 'switch', 'source': 'ARN'},
                     'doc_service': {'call': 'switch', 'source': 'DocService'},
                     'search_service': {'call': 'switch', 'source': 'SearchService'},
                     'requires_index_documents': {'call': 'switch', 'source': 'RequiresIndexDocuments'},
                     'processing': {'call': 'switch', 'source': 'Processing'},
                     'search_instance_type': {'call': 'switch', 'source': 'SearchInstanceType'},
                     'search_partition_count': {'call': 'switch', 'source': 'SearchPartitionCount'},
                     'search_instance_count': {'call': 'switch', 'source': 'SearchInstanceCount'},
                     'limits': {'call': 'switch', 'source': 'Limits'}
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
