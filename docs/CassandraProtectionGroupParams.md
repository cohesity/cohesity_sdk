# CassandraProtectionGroupParams

Specifies the parameters for Cassandra Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_scale_concurrency** | **bool** | Specifies the flag to automatically scale number of concurrent IO Streams that will be created to exchange data with the cluster. | [optional] 
**bandwidth_mbps** | **int** | Specifies the maximum network bandwidth that each concurrent IO Stream can use for exchanging data with the cluster. | [optional] 
**concurrency** | **int** | Specifies the maximum number of concurrent IO Streams that will be created to exchange data with the cluster. | [optional] 
**custom_source_name** | **str** | The user specified name for the Source on which this protection was run. | [optional] [readonly] 
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**objects** | [**List[NoSqlProtectionGroupObjectParams]**](NoSqlProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**source_id** | **int** | Object ID of the Source on which this protection was run . | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the Source on which this protection was run. | [optional] [readonly] 
**data_centers** | **List[str]** | Only the specified data centers will be considered while taking backup. The keyspaces having replication strategy &#39;Simple&#39; can be backed up only if all the datacenters for the cassandra cluster are specified. For any keyspace having replication strategy as &#39;Network&#39;, all the associated data centers should be specified. | [optional] 
**is_log_backup** | **bool** | Specifies the type of job for Cassandra. If true, only log backup job will be scheduled for the source. This requires a policy with log Backup option enabled. | [optional] 
**is_system_keyspace_backup** | **bool** | Specifies whether this ia a system keyspace backup job. | [optional] 

## Example

```python
from cohesity_sdk.models.cassandra_protection_group_params import CassandraProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of CassandraProtectionGroupParams from a JSON string
cassandra_protection_group_params_instance = CassandraProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(CassandraProtectionGroupParams.to_json())

# convert the object into a dict
cassandra_protection_group_params_dict = cassandra_protection_group_params_instance.to_dict()
# create an instance of CassandraProtectionGroupParams from a dict
cassandra_protection_group_params_from_dict = CassandraProtectionGroupParams.from_dict(cassandra_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


