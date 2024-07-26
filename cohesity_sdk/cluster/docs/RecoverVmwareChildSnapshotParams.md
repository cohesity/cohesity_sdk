# RecoverVmwareChildSnapshotParams

Specifies the snapshot parameters for VMware recovery.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_id** | **str** | Specifies the snapshot id. | 
**archival_target_info** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the archival target information if the snapshot is an archival snapshot. | [optional] 
**bytes_restored** | **int, none_type** | Specify the total bytes restored. | [optional] [readonly] 
**end_time_usecs** | **int, none_type** | Specifies the end time of the Recovery in Unix timestamp epoch in microseconds. This field will be populated only after Recovery is finished. | [optional] [readonly] 
**messages** | **[str], none_type** | Specify error messages about the object. | [optional] [readonly] 
**object_info** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the information about the object for which the snapshot is taken. | [optional] 
**point_in_time_usecs** | **int, none_type** | Specifies the timestamp (in microseconds. from epoch) for recovering to a point-in-time in the past. | [optional] 
**progress_task_id** | **str, none_type** | Progress monitor task id for Recovery of VM. | [optional] [readonly] 
**protection_group_id** | **str, none_type** | Specifies the protection group id of the object snapshot. | [optional] 
**protection_group_name** | **str, none_type** | Specifies the protection group name of the object snapshot. | [optional] 
**recover_from_standby** | **bool, none_type** | Specifies that user wants to perform standby restore if it is enabled for this object. | [optional] 
**snapshot_creation_time_usecs** | **int, none_type** | Specifies the time when the snapshot is created in Unix timestamp epoch in microseconds. | [optional] [readonly] 
**snapshot_target_type** | **str, none_type** | Specifies the snapshot target type. | [optional] [readonly] 
**start_time_usecs** | **int, none_type** | Specifies the start time of the Recovery in Unix timestamp epoch in microseconds. | [optional] [readonly] 
**status** | **str, none_type** | Status of the Recovery. &#39;Running&#39; indicates that the Recovery is still running. &#39;Canceled&#39; indicates that the Recovery has been cancelled. &#39;Canceling&#39; indicates that the Recovery is in the process of being cancelled. &#39;Failed&#39; indicates that the Recovery has failed. &#39;Succeeded&#39; indicates that the Recovery has finished successfully. &#39;SucceededWithWarning&#39; indicates that the Recovery finished successfully, but there were some warning messages. &#39;Skipped&#39; indicates that the Recovery task was skipped. | [optional] [readonly] 
**storage_domain_id** | **int, none_type** | Specifies the ID of the Storage Domain where this snapshot is stored. | [optional] [readonly] 
**datastore_migration_info** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the info about datastore migration. This is only applicable for RecoverVm. | [optional] 
**instant_recovery_info** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the info about instant recovery. This is only applicable for RecoverVm. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


