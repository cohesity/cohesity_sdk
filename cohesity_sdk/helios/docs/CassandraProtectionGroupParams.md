# CassandraProtectionGroupParams

Specifies the parameters for Cassandra Protection Group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[NoSqlProtectionGroupObjectParams]**](NoSqlProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**concurrency** | **int, none_type** | Specifies the maximum number of concurrent IO Streams that will be created to exchange data with the cluster. | [optional] 
**bandwidth_mbps** | **int, none_type** | Specifies the maximum network bandwidth that each concurrent IO Stream can use for exchanging data with the cluster. | [optional] 
**exclude_object_ids** | **[int], none_type** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**source_id** | **int, none_type** | Object ID of the Source on which this protection was run . | [optional] [readonly] 
**source_name** | **str, none_type** | Specifies the name of the Source on which this protection was run. | [optional] [readonly] 
**custom_source_name** | **str, none_type** | The user specified name for the Source on which this protection was run. | [optional] [readonly] 
**data_centers** | **[str]** | Only the specified data centers will be considered while taking backup. The keyspaces having replication strategy &#39;Simple&#39; can be backed up only if all the datacenters for the cassandra cluster are specified. For any keyspace having replication strategy as &#39;Network&#39;, all the associated data centers should be specified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


