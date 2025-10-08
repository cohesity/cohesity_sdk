# HypervEnvJobParams

Specifies job parameters applicable for all 'kHyperV' Environment type Protection Sources in a Protection Job.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_disks** | [**[HyperVDiskInfo], none_type**](HyperVDiskInfo.md) | Specifies a list of disks to exclude from being protected for the object/vm. | [optional] 
**fallback_to_crash_consistent** | **bool, none_type** | If true, takes a crash-consistent snapshot when app-consistent snapshot fails. Otherwise, the snapshot attempt is marked failed. | [optional] 
**include_disks** | [**[HyperVDiskInfo], none_type**](HyperVDiskInfo.md) | Specifies a list of disks to included in the protection for the object/vm. | [optional] 
**protection_type** | **str, none_type** | Specifies the Protection Group type. If not specified, then backup method is auto determined. Specifying RCT will forcibly use RCT backup for all VMs in this Protection Group. Available only for VMs with hardware version 8.0 and above, but is more efficient. Specifying VSS will forcibly use VSS backup for all VMs in this Protection Group. Available for VMs with hardware version 5.0 and above, but is slower than RCT backup. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


