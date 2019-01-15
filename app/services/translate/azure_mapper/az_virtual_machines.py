def rules(conn):
    return {
        'hostname': {'call': 'switch', 'source': 'name'},
        'unique_id': {'call': 'createID', 'source': {
            'key': 'id',
            'reg': r'^\/subscriptions/(.*)/resourceGroups/(.*)/providers/Microsoft.Compute/virtualMachines/(.*)?'
        }},

        'datacenters': {'call': 'fctDc',
                        'source': {**conn}},

        'created_at': {'call': 'now'},
        'updated_at': {'call': 'now'},
        'environment': {'call': 'switch', 'source': 'tags.environment'},
        'role': {'call': 'switch', 'source': 'tags.role'},

        'tags': {'call': 'fctTags', 'source': 'tags'},
        'applications': {'call': 'SyncForeignEntityByTag', 'source': {
            'field': 'tags.applications',
            'resource': 'applications'
        }},

        'os': {'call': 'fcOS', 'source': 'storage_profile'},
        'storage': {'call': 'fcStorage', 'source': 'storage_profile'},

        'status': {'call': 'switchOptions',
                   'source': {'field': 'provisioning_state',
                              'options': {
                                  "Succeeded": "Active"
                              },
                              'default': "Avaliable"
                              }},

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
