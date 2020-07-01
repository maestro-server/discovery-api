def rules(conn):
    return {
        'hostname': {'call': 'switch', 'source': 'ansible_nodename'},
        'ipv4_private': {'call': 'switch', 'source': 'ansible_default_ipv4.address'},
        'ipv4_public': {'call': 'switch', 'source': 'ansible_default_ipv6.address'},

        'cpu': {'call': 'switch', 'source': 'ansible_processor_vcpus'},
        'memory': {'call': 'getMemory', 'source': 'ansible_memtotal_mb'},

        'os': {'call': 'getOs'},

        'storage': {'call': 'getStorages', 'source': 'ansible_devices'},
        'storage_count': {'call': 'countItem', 'source': 'ansible_devices'},
        'env_vars': {'call': 'switch', 'source': 'ansible_env'},
        'dns': {'call': 'switch', 'source': 'ansible_dns'},
        'network_lo': {'call': 'switch', 'source': 'ansible_lo'},
        'network_interface': {'call': 'switch', 'source': 'ansible_interfaces'},
        'service_mgr': {'call': 'switch', 'source': 'ansible_service_mgr'},
        'pkg_mgr': {'call': 'switch', 'source': 'ansible_pkg_mgr'},

        'ipv4_all': {'call': 'switch', 'source': 'ansible_all_ipv4_addresses'},
        'ipv6_all': {'call': 'switch', 'source': 'ansible_all_ipv6_addresses'},

        'auth': {'call': 'getAuth', 'source': 'ansible_user_id'},

        'services': {'call': 'getService'},

        'datacenters': {'call': 'fctDc',
                        'source': {**conn}},
        'active': {'call': 'setV', 'source': True},

        'accountant': {'call': 'fctAccountant', 'source': {**conn}},

        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}},
        'checksum': {'call': 'checksum',
                     'source': None}
    }
