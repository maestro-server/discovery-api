def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'attributes.tags.name|attributes.tags.Name'},
        'cpu': {'call': 'switch', 'source': 'attributes.cpu_core_count'},
        'unique_id': {'call': 'switch', 'source': 'attributes.id'},

        'role': {'call': 'switch', 'source': 'attributes.tags.role|attributes.tags.Role'},
        'environment': {'call': 'switch', 'source': 'attributes.tags.environment|attributes.tags.env'},

        'dns_public': {'call': 'switch', 'source': 'attributes.public_dns'},
        'dns_private': {'call': 'switch', 'source': 'attributes.private_dns'},

        'ebs_optimized': {'call': 'switch', 'source': 'attributes.ebs_optimized'},

        'ipv4_private': {'call': 'switch', 'source': 'attributes.private_ip'},
        'ipv4_public': {'call': 'switch', 'source': 'attributes.public_ip'},

        'storage': {'call': 'fctStorage', 'source': 'attributes.ebs_block_device|attributes.root_block_device'},
        'auth': {'call': 'fctAuth', 'source': 'attributes.key_name'},
        'status': {'call': 'switchOptions',
                   'source': {'field': 'attributes.instance_state',

                              'options': {'running': 'Active', 'pending': 'Active', 'stopping': 'Stopped',
                                          'stopped': 'Stopped'},
                              'default': None
                              }},

        'tags': {'call': 'fctTags', 'source': 'attributes.tags'},

        'datacenters': {'call': 'fctDc',
                        'source': {**conn}},

        'active': {'call': 'setV', 'source': True},

        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'accountant': {'call': 'fctAccountant', 'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}},
        'checksum': {'call': 'checksum',
                     'source': None}
    }
