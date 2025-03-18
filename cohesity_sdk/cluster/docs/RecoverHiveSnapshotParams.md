# RecoverHiveSnapshotParams

Specifies the snapshot parameters for a protected Hive object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_target_info** | [**ArchivalTargetSummaryInfo**](ArchivalTargetSummaryInfo.md) |  | [optional] 
**bytes_restored** | **int** | Specify the total bytes restored. | [optional] [readonly] 
**end_time_usecs** | **int** | Specifies the end time of the Recovery in Unix timestamp epoch in microseconds. This field will be populated only after Recovery is finished. | [optional] [readonly] 
**messages** | **List[str]** | Specify error messages about the object. | [optional] [readonly] 
**object_info** | [**ObjectSummary**](ObjectSummary.md) |  | [optional] 
**point_in_time_usecs** | **int** | Specifies the timestamp (in microseconds. from epoch) for recovering to a point-in-time in the past. | [optional] 
**progress_task_id** | **str** | Progress monitor task id for Recovery of VM. | [optional] [readonly] 
**protection_group_id** | **str** | Specifies the protection group id of the object snapshot. | [optional] 
**protection_group_name** | **str** | Specifies the protection group name of the object snapshot. | [optional] 
**recover_from_standby** | **bool** | Specifies that user wants to perform standby restore if it is enabled for this object. | [optional] 
**snapshot_creation_time_usecs** | **int** | Specifies the time when the snapshot is created in Unix timestamp epoch in microseconds. | [optional] [readonly] 
**snapshot_id** | **str** | Specifies the snapshot id. | 
**snapshot_target_type** | **str** | Specifies the snapshot target type. | [optional] [readonly] 
**start_time_usecs** | **int** | Specifies the start time of the Recovery in Unix timestamp epoch in microseconds. | [optional] [readonly] 
**status** | **str** | Status of the Recovery. &#39;Running&#39; indicates that the Recovery is still running. &#39;Canceled&#39; indicates that the Recovery has been cancelled. &#39;Canceling&#39; indicates that the Recovery is in the process of being cancelled. &#39;Failed&#39; indicates that the Recovery has failed. &#39;Succeeded&#39; indicates that the Recovery has finished successfully. &#39;SucceededWithWarning&#39; indicates that the Recovery finished successfully, but there were some warning messages. &#39;Skipped&#39; indicates that the Recovery task was skipped. | [optional] [readonly] 
**storage_domain_id** | **int** | Specifies the ID of the Storage Domain where this snapshot is stored. | [optional] [readonly] 
**objects** | [**List[RecoverHiveNoSqlObjectParams]**](RecoverHiveNoSqlObjectParams.md) | Specifies details of objects to be recovered. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_hive_snapshot_params import RecoverHiveSnapshotParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverHiveSnapshotParams from a JSON string
recover_hive_snapshot_params_instance = RecoverHiveSnapshotParams.from_json(json)
# print the JSON string representation of the object
print(RecoverHiveSnapshotParams.to_json())

# convert the object into a dict
recover_hive_snapshot_params_dict = recover_hive_snapshot_params_instance.to_dict()
# create an instance of RecoverHiveSnapshotParams from a dict
recover_hive_snapshot_params_from_dict = RecoverHiveSnapshotParams.from_dict(recover_hive_snapshot_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


