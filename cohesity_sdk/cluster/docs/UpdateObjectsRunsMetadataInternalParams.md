# UpdateObjectsRunsMetadataInternalParams

Specifies the params for updating one or more runs of one or more objects via the cluster's internal API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | Specifies the environment. | [optional] 
**legal_hold** | **str, none_type** | Specifies whether to retain the snapshot for legal purpose. If set to &#39;enable&#39;, the snapshots cannot be deleted until the retention period. Note that using this option may cause the Cluster to run out of space. This field can be set only by a User having Data Security Role.  If set to &#39;release&#39;, the snapshots under legal hold will be released. | [optional] 
**retention** | [**Retention**](Retention.md) |  | [optional] 
**target_object_runs** | [**[TargetObjectRun]**](TargetObjectRun.md) | An array of objects. Each containing object id and the run start time that we want to target. | [optional] 
**time_range** | [**TimeRangeUsecs**](TimeRangeUsecs.md) |  | [optional] 
**tenant_id** | **str, none_type** | Tenant id associated with the incoming request | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


