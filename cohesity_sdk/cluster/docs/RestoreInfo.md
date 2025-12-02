# RestoreInfo

Specifies the info regarding a snapshot

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_target_info** | [**ArchivalTargetSummaryInfo**](ArchivalTargetSummaryInfo.md) |  | [optional] 
**attempt_number** | **int** | Specifies the attempt number of the job run to restore from. | [optional] 
**cloud_deploy_target** | [**CloudSpinTarget**](CloudSpinTarget.md) |  | [optional] 
**cloud_replication_target** | [**CloudSpinTarget**](CloudSpinTarget.md) |  | [optional] 
**object_info** | [**Object**](Object.md) |  | [optional] 
**parent_object_info** | [**Object**](Object.md) |  | [optional] 
**protection_group_id** | **str** | Specifies the protection group id of the run responsible for the snapshot | [optional] 
**run_start_time_usecs** | **int** | Specifies the start time specified as a Unix epoch Timestamp (in microseconds). | [optional] 
**snapshot_relative_dir_path** | **str** | Specifies the relative path to the directory containing the entity&#39;s snapshot. | [optional] 
**view_name** | **str** | The name of the view where the object&#39;s snapshot is located. | [optional] 
**vm_had_independent_disks** | **bool** | Specifies this is applicable only to VMs and is set to true when the VM being recovered or cloned contained independent disks when it was backed up. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.restore_info import RestoreInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreInfo from a JSON string
restore_info_instance = RestoreInfo.from_json(json)
# print the JSON string representation of the object
print(RestoreInfo.to_json())

# convert the object into a dict
restore_info_dict = restore_info_instance.to_dict()
# create an instance of RestoreInfo from a dict
restore_info_from_dict = RestoreInfo.from_dict(restore_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


