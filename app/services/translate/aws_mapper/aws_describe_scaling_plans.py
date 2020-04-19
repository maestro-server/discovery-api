def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'ScalingPlanName'},
        'unique_id': {'call': 'switch', 'source': 'ScalingPlanName'},

        'scaling_plan_version': {'call': 'switch', 'source': 'ScalingPlanVersion'},
        'scaling_plan_name': {'call': 'switch', 'source': 'ScalingPlanName'},

        'role': {'call': 'batch',
                 'source': {
                     'scaling_plan_version': {'call': 'switch', 'source': 'ScalingPlanVersion'},
                     'scaling_planName': {'call': 'switch', 'source': 'ScalingPlanName'},
                     'scaling_instructions': {'call': 'switch', 'source': 'ScalingInstructions'}
                 }
                 },
        'status': {'call': 'switchCapitalized', 'source': 'StatusCode'},
        'status_message': {'call': 'switch', 'source': 'StatusMessage'},

        'datacenters': {'call': 'fctDcApp',
                        'source': {**conn}},

        'active': {'call': 'switchOptions',
                   'source': {'field': 'StatusCode',
                              'options': {
                                  'CreationFailed': False,
                                  'DeletionInProgress': False,
                                  'DeletionFailed': False,
                                  'UpdateFailed': False
                              },
                              'default': True
                              }},

        'environment': {'call': 'arrCatcher',
                        'source': {'field': 'Tags', 'sKey': 'Key', 's': 'environment', 'catcher': 'Value'}},
        'created_at': {'call': 'switch', 'source': 'CreatedTime'},
        'updated_at': {'call': 'switch', 'source': 'CreatedTime'},
        'provider': {'call': 'setV', 'source': 'AutoScaling (AWS)'},
        'own': {'call': 'setV', 'source': 1},
        'tags': {'call': 'fctTags', 'source': 'Tags'},
        'family': {'call': 'setV', 'source': 'AutoScalingPlan'},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}},
        'checksum': {'call': 'checksum',
                     'source': None}
    }
