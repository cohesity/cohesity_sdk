# HyperVProtectionGroupObjectParams

Specifies the object parameters to create HyperV Protection Group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | Specifies the id of the object. | 
**exclude_disks** | [**[HyperVDiskInfo], none_type**](HyperVDiskInfo.md) | Specifies a list of disks to exclude from being protected for the object/vm. | [optional] 
**include_disks** | [**[HyperVDiskInfo], none_type**](HyperVDiskInfo.md) | Specifies a list of disks to included in the protection for the object/vm. | [optional] 
**name** | **str, none_type** | Specifies the name of the virtual machine. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


