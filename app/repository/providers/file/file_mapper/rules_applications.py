def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'name'},
        'unique_id': {'call': 'switch', 'source': 'unique_id'},
        'asm_groups': {'call': 'switch', 'source': 'asm_groups'},
        'spec': {'call': 'switch', 'source': 'spec'},
        'size': {'call': 'switch', 'source': 'size'},

        'engine': {'call': 'switch', 'source': 'engine'},
        'system': {'call': 'switch', 'source': 'system'},

        'own': {'call': 'switch', 'source': 'own'},
        'provider': {'call': 'switch', 'source': 'provider'},
        'tags': {'call': 'switch', 'source': 'tags'},
        'environment': {'call': 'switch', 'source': 'environment'},

        'family': {'call': 'switch', 'source': 'family'},
        'status': {'call': 'switch', 'source': 'status'},

        'domain': {'call': 'switch', 'source': 'domain'},
        'loadbalance_names': {'call': 'switch', 'source': 'loadbalance_names'},
        'instances': {'call': 'switch', 'source': 'instances'},

        'language': {'call': 'switch', 'source': 'language'},
        'cluster': {'call': 'switch', 'source': 'cluster'},
        'dataguard': {'call': 'switch', 'source': 'dataguard'},
        'type': {'call': 'switch', 'source': 'type'},
        'storage_types': {'call': 'switch', 'source': 'storage_types'},
        'queues': {'call': 'switch', 'source': 'queues'},

        'urls': {'call': 'switch', 'source': 'urls'},
        'cache_behavior': {'call': 'switch', 'source': 'cache_behavior'},
        'cache_nodes': {'call': 'switch', 'source': 'cache_nodes'},
        'crs_version': {'call': 'switch', 'source': 'crs_version'},
        'modal': {'call': 'switch', 'source': 'modal'},
        'pdbs': {'call': 'switch', 'source': 'pdbs'},

        'active': {'call': 'setV', 'source': True},
        'datacenters': {'call': 'fctDc',
                        'source': {**conn}},

        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'accountant': {'call': 'fctAccountant', 'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}},
        'checksum': {'call': 'checksum',
                     'source': None}
    }
