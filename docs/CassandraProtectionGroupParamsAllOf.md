# CassandraProtectionGroupParamsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_centers** | **[str]** | Only the specified data centers will be considered while taking backup. The keyspaces having replication strategy &#39;Simple&#39; can be backed up only if all the datacenters for the cassandra cluster are specified. For any keyspace having replication strategy as &#39;Network&#39;, all the associated data centers should be specified. | [optional] 
**is_log_backup** | **bool, none_type** | Specifies the type of job for Cassandra. If true, only log backup job will be scheduled for the source. This requires a policy with log Backup option enabled. | [optional] 
**is_system_keyspace_backup** | **bool, none_type** | Specifies whether this ia a system keyspace backup job. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


