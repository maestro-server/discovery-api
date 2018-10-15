def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'DBInstanceIdentifier'},
        'engine': {'call': 'switch', 'source': 'Engine'},
        'unique_id': {'call': 'switch', 'source': 'DBInstanceIdentifier'},


        'role': {'call': 'batch',
                 'source': {
                    'dbname': {'call': 'switch', 'source': 'DBName'},
                    'endpoint': {'call': 'switch', 'source': 'Endpoint'},
                    'allocated_storage': {'call': 'switch', 'source': 'AllocatedStorage'},
                    'backup_window': {'call': 'switch', 'source': 'PreferredBackupWindow'},
                    'backup_retention': {'call': 'switch', 'source': 'BackupRetentionPeriod'},
                    'security_group': {'call': 'switch', 'source': 'DBSecurityGroups'},
                    'class': {'call': 'switch', 'source': 'DBInstanceClass'},
                    'parameter': {'call': 'switch', 'source': 'DBParameterGroups'},
                    'vpc_security': {'call': 'switch', 'source': 'VpcSecurityGroups'},
                    'subnet_group': {'call': 'switch', 'source': 'DBSubnetGroup'},
                    'availability_zone': {'call': 'switch', 'source': 'AvailabilityZone'},
                    'read_replica': {'call': 'switch', 'source': 'ReadReplicaDBClusterIdentifiers'},
                    'license_model': {'call': 'switch', 'source': 'LicenseModel'},
                    'iops': {'call': 'switch', 'source': 'Iops'},
                    'secondary_availability_zone': {'call': 'switch', 'source': 'SecondaryAvailabilityZone'},
                    'storage_type': {'call': 'switch', 'source': 'StorageType'},
                    'instance_port': {'call': 'switch', 'source': 'DbInstancePort'},
                    'cluster_name': {'call': 'switch', 'source': 'DBClusterIdentifier'},
                    'storage_encrypted': {'call': 'switch', 'source': 'StorageEncrypted'},
                    'domain': {'call': 'switch', 'source': 'DomainMemberships'},
                    'monitoring_interval': {'call': 'switch', 'source': 'MonitoringInterval'},
                    'instance_arn': {'call': 'switch', 'source': 'DBInstanceArn'},
                    'timezone': {'call': 'switch', 'source': 'Timezone'},
                    'cloudwatch_export': {'call': 'switch', 'source': 'EnabledCloudwatchLogsExports'}
                    }
                 },


        'status': {'call': 'switch', 'source': 'DBInstanceStatus'},
        'read_status': {'call': 'switch', 'source': 'StatusInfos.Status'},

        'datacenters': {'call': 'fctDcApp',
                        'source': {**conn}},
        'active': {'call': 'switchOptions',
                   'source': {'field': 'DBInstanceStatus',
                              'options': {'stopping': False, 'stopped': False, 'failed': False, 'deleting': False, 'inaccessible-encryption-credentials': False, 'incompatible-network': False},
                              'default': True
                              }},
        'environment': {'call': 'arrCatcher',
                        'source': {'field': 'Tags', 'sKey': 'Key', 's': 'environment', 'catcher': 'Value'}},
        'created_at': {'call': 'switch', 'source': 'CreatedTime'},
        'provider': {'call': 'setV', 'source': 'RDS (AWS)'},
        'own': {'call': 'setV', 'source': 1},
        'tags': {'call': 'fctTags', 'source': 'Tags'},
        'family': {'call': 'setV', 'source': 'Database'},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}},
        'checksum': {'call': 'checksum',
                     'source': None}
    }
