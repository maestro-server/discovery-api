def rules(conn):
    return {
        'name': {'call': 'switch', 'source': 'ReplicationGroupId'},
        'unique_id': {'call': 'switch', 'source': 'CacheClusterId'},

        'created_at': {'call': 'switch', 'source': 'CacheClusterCreateTime'},

        'provider': {'call': 'setV', 'source': 'Elastic Cache (AWS)'},
        'family': {'call': 'setV', 'source': 'Cache'},
        'active': {'call': 'setV', 'source': True},

        'engine': {'call': 'switch', 'source': 'Engine'},

        'role': {'call': 'batch',
                 'source': {
                     'configuration_endpoint': {'call': 'switch', 'source': 'ConfigurationEndpoint'},
                     'client_download_landing_page': {'call': 'switch', 'source': 'ClientDownloadLandingPage'},
                     'cache_node_type': {'call': 'switch', 'source': 'CacheNodeType'},
                     'engine_version': {'call': 'switch', 'source': 'EngineVersion'},
                     'cache_cluster_status': {'call': 'switch', 'source': 'CacheClusterStatus'},
                     'num_cache_nodes': {'call': 'switch', 'source': 'NumCacheNodes'},
                     'preferred_availability_zone': {'call': 'switch', 'source': 'PreferredAvailabilityZone'},
                     'cache_cluster_create_time': {'call': 'switch', 'source': 'CacheClusterCreateTime'},
                     'preferred_maintenance_window': {'call': 'switch', 'source': 'PreferredMaintenanceWindow'},
                     'pending_modified_values': {'call': 'switch', 'source': 'PendingModifiedValues'},
                     'engine': {'call': 'switch', 'source': 'Engine'},
                     'engine_version': {'call': 'switch', 'source': 'EngineVersion'},
                     'cache_cluster_status': {'call': 'switch', 'source': 'CacheClusterStatus'},
                     'notification_configuration': {'call': 'switch', 'source': 'NotificationConfiguration'},
                     'preferred_availability_zone': {'call': 'switch', 'source': 'PreferredAvailabilityZone'},
                     'cache_subnet_group_name': {'call': 'switch', 'source': 'CacheSubnetGroupName'},
                     'replication_group_id': {'call': 'switch', 'source': 'ReplicationGroupId'},
                     'snapshot_retention_limit': {'call': 'switch', 'source': 'SnapshotRetentionLimit'},
                     'snapshot_window': {'call': 'switch', 'source': 'SnapshotWindow'},
                     'auth_token_enabled': {'call': 'switch', 'source': 'AuthTokenEnabled'},
                     'transit_encryption_enabled': {'call': 'switch', 'source': 'TransitEncryptionEnabled'},
                     'atRest_encryption_enabled': {'call': 'switch', 'source': 'AtRestEncryptionEnabled'},
                 }
                 },

        'cache_nodes': {'call': 'switch', 'source': 'CacheNodes'},

        'datacenters': {'call': 'fctDcApp',
                        'source': {**conn}},
        'accountant': {'call': 'fctAccountant', 'source': {**conn}},
        'own': {'call': 'setV', 'source': 1},
        'owner': {'call': 'fctOwner',
                  'source': {**conn}},
        'roles': {'call': 'fctRoles',
                  'source': {**conn}},
        'checksum': {'call': 'checksum',
                     'source': None}
    }
