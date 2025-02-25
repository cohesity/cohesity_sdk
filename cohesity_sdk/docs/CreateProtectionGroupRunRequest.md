# CreateProtectionGroupRunRequest

Specifies the request to create a protection run. On success, the system will accept the request and return the Protection Group id for which the run is supposed to start. The actual run may start at a later time if the system is busy. Consumers must query the Protection Group to see the run.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_type** | **str, none_type** | Type of protection run. &#39;kRegular&#39; indicates an incremental (CBT) backup. Incremental backups utilizing CBT (if supported) are captured of the target protection objects. The first run of a kRegular schedule captures all the blocks. &#39;kFull&#39; indicates a full (no CBT) backup. A complete backup (all blocks) of the target protection objects are always captured and Change Block Tracking (CBT) is not utilized. &#39;kLog&#39; indicates a Database Log backup. Capture the database transaction logs to allow rolling back to a specific point in time. &#39;kSystem&#39; indicates system volume backup. It produces an image for bare metal recovery. | 
**cassandra_params** | [**CassandraProtectionRunParams**](CassandraProtectionRunParams.md) |  | [optional] 
**objects** | [**[RunObject]**](RunObject.md) | Specifies the list of objects to be protected by this Protection Group run. These can be leaf objects or non-leaf objects in the protection hierarchy. This must be specified only if a subset of objects from the Protection Groups needs to be protected. | [optional] 
**targets_config** | [**RunTargetsConfiguration**](RunTargetsConfiguration.md) |  | [optional] 
**uda_params** | [**UdaProtectionRunParams**](UdaProtectionRunParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


