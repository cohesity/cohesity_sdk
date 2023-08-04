# AcropolisProtectionGroupObjectParams

Specifies an object protected by a Acropolis Protection Group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | Specifies the ID of the object. | 
**name** | **str, none_type** | Specifies the name of the virtual machine. | [optional] [readonly] 
**exclude_disks** | [**[AcropolisDiskInfo], none_type**](AcropolisDiskInfo.md) | Specifies a list of disks to exclude from being protected. This is only applicable to VM objects. | [optional] 
**include_disks** | [**[AcropolisDiskInfo], none_type**](AcropolisDiskInfo.md) | Specifies a list of disks to include in the protection. This is only applicable to VM objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


