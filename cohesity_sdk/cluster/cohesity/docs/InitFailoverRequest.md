# InitFailoverRequest

Specifies the failover request parameters to initiate a failover.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protection_group_environment** | **str, none_type** | If this field is specified then protection groups will be looked up only for this specific environment | [optional] 
**replication_cluster** | [**FailoverReplicaCluster**](FailoverReplicaCluster.md) |  | [optional] 
**source_cluster** | [**FailoverSourceCluster**](FailoverSourceCluster.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


