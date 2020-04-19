def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'name'},
        'unique_id': {'call': 'createID', 'source': {
            'key': 'id',
            'reg': r'^\/subscriptions/(.*)/resourceGroups/(.*)/providers/Microsoft.Network/virtualNetworks/(.*)?'
        }},

        'datacenters': {'call': 'fctDc',
                        'source': {**conn}},

        'environment': {'call': 'switch', 'source': 'tags.environment'},
        'subnets': {'call': 'serialize', 'source': 'subnets'},
        'address_space': {'call': 'serialize', 'source': 'address_space'},
        'virtual_network_peerings': {'call': 'serialize', 'source': 'virtual_network_peerings'},

        'enable_vm_protection': {'call': 'switch', 'source': 'enable_vm_protection'},
        'enable_ddos_protection': {'call': 'switch', 'source': 'enable_ddos_protection'},
        'type': {'call': 'switch', 'source': 'type'},
        'dhcp_options': {'call': 'switch', 'source': 'dhcp_options'},
        'ddos_protection_plan': {'call': 'serialize', 'source': 'ddos_protection_plan'},

        'family': {'call': 'setV', 'source': 'VirtualNetwork'},
        'tags': {'call': 'fctTags', 'source': 'tags'},

        'active': {'call': 'switchOptions',
                   'source': {'field': 'status',
                              'options': {},
                              'default': True
                              }},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}},
        'checksum': {'call': 'checksum',
                     'source': None}
    }
