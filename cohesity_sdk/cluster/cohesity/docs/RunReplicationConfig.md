# RunReplicationConfig

Specifies settings for copying Snapshots to Remote Clusters. This also specifies the retention policy that should be applied to Snapshots after they have been copied to the specified target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | Specifies id of Remote Cluster to copy the Snapshots to. | 
**name** | **str, none_type** | Specifies the cluster name of the replication cluster. | [optional] 
**object_ids** | **[str, none_type], none_type** | Specifies the list of object as string ids to be replicated by this Protection Group run. These can be leaf objects or non-leaf objects in the protection hierarchy. This must be specified only if a subset of objects from the Protection Group needs to be replicated. | [optional] 
**on_legal_hold** | **bool, none_type** | Specifies if the Run is on legal hold. | [optional] 
**retention** | [**Retention**](Retention.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


