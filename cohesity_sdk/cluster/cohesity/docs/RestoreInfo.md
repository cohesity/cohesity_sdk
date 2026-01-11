# RestoreInfo

Specifies the info regarding a snapshot

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_target_info** | [**ArchivalTargetSummaryInfo**](ArchivalTargetSummaryInfo.md) |  | [optional] 
**attempt_number** | **int, none_type** | Specifies the attempt number of the job run to restore from. | [optional] 
**cloud_deploy_target** | [**CloudSpinTarget**](CloudSpinTarget.md) |  | [optional] 
**cloud_replication_target** | [**CloudSpinTarget**](CloudSpinTarget.md) |  | [optional] 
**object_info** | [**Object**](Object.md) |  | [optional] 
**parent_object_info** | [**Object**](Object.md) |  | [optional] 
**protection_group_id** | **str, none_type** | Specifies the protection group id of the run responsible for the snapshot | [optional] 
**run_start_time_usecs** | **int, none_type** | Specifies the start time specified as a Unix epoch Timestamp (in microseconds). | [optional] 
**snapshot_relative_dir_path** | **str, none_type** | Specifies the relative path to the directory containing the entity&#39;s snapshot. | [optional] 
**view_name** | **str, none_type** | The name of the view where the object&#39;s snapshot is located. | [optional] 
**vm_had_independent_disks** | **bool, none_type** | Specifies this is applicable only to VMs and is set to true when the VM being recovered or cloned contained independent disks when it was backed up. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


