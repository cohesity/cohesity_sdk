# VmwareEnvJobParams

Specifies job parameters applicable for all 'kVMware' Environment type Protection Sources in a Protection Job.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excluded_disks** | [**[DiskInfo], none_type**](DiskInfo.md) | Specifies the list of Disks to be excluded from backing up. These disks are excluded from all Protection Sources in the Protection Job. | [optional] 
**fallback_to_crash_consistent** | **bool, none_type** | If true, takes a crash-consistent snapshot when app-consistent snapshot fails. Otherwise, the snapshot attempt is marked failed. | [optional] 
**skip_physical_rdm_disks** | **bool, none_type** | If true, skip physical RDM disks when backing up VMs. Otherwise, backup of VMs having physical RDM will fail. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


