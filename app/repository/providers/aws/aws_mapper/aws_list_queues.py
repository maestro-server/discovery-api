def rules(conn):
    return {
        'name|unique_id|urls|queues': {'call': 'QueueSQS', 'source': 'QueueUrls', 'merged': True},

        'provider': {'call': 'setV', 'source': 'SQS (AWS)'},
        'family': {'call': 'setV', 'source': 'Broker'},
        'active': {'call': 'setV', 'source': True},

        'datacenters': {'call': 'fctDcApp',
                        'source': {**conn}},
        'own': {'call': 'setV', 'source': 1},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'accountant': {'call': 'fctAccountant', 'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}},
        'checksum': {'call': 'checksum',
                     'source': None}
    }
