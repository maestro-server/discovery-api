def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'name'},
        'unique_id': {'call': 'switch', 'source': 'unique_id'},
        'image_type': {'call': 'switch', 'source': 'image_type'},
        'image_location': {'call': 'switch', 'source': 'image_location'},
        'status': {'call': 'switch', 'source': 'status'},

        'root_device_type': {'call': 'switch', 'source': 'root_device_type'},

        'hypervisor': {'call': 'switch', 'source': 'hypervisor'},
        'plataform': {'call': 'switch', 'source': 'plataform'},
        'tags': {'call': 'switch', 'source': 'tags'},
        'storage': {'call': 'switch', 'source': 'storage'},

        'distribution': {'call': 'switch', 'source': 'distribution'},
        'slug': {'call': 'switch', 'source': 'slug'},
        'region': {'call': 'switch', 'source': 'region'},

        'public': {'call': 'switch', 'source': 'public'},
        'min_disk_size': {'call': 'switch', 'source': 'min_disk_size'},
        'type': {'call': 'switch', 'source': 'type'},

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
