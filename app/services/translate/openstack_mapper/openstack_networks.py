def rules(conn):
    return {
        'unique_id': {'call': 'switch', 'source': 'id'},
        'description': {'call': 'switch', 'source': 'description'},
        'status': {'call': 'switch', 'source': 'status'},
        'subnet_ids': {'call': 'switch', 'source': 'subnet_ids'},
        'project_id': {'call': 'switch', 'source': 'project_id'},
        'mtu': {'call': 'switch', 'source': 'mtu'},
        'ipv4_address_scope_id': {'call': 'switch', 'source': 'ipv4_address_scope_id'},
        'is_port_security_enabled': {'call': 'switch', 'source': 'is_port_security_enabled'},
        'service': {'call': 'switch', 'source': 'service'},
        'ipv6_address_scope_id': {'call': 'switch', 'source': 'ipv6_address_scope_id'},
        'name': {'call': 'switch', 'source': 'name'},
        'is_vlan_transparent': {'call': 'switch', 'source': 'is_vlan_transparent'},
        'own': {'call': 'setV', 'source': 1},
        'family': {'call': 'setV', 'source': 'Network'},
        'datacenters': {'call': 'fctDcApp',
                        'source': {**conn}},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'active': {'call': 'setV', 'source': True},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}}
    }
