# VmwareObjectProtectionResponse

Specifies the input for a protection object in the VMware environment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_disks** | [**[DiskInfo], none_type**](DiskInfo.md) | Specifies a list of disks to exclude from being protected. This is only applicable to VM objects. | [optional] 
**truncate_exchange_logs** | **bool, none_type** | Specifies whether or not to truncate MS Exchange logs while taking an app consistent snapshot of this object. This is only applicable to objects which have a registered MS Exchange app. | [optional] 
**exclude_object_ids** | **[int, none_type]** | Specifies the list of IDs of the objects to not be protected in this backup. This field only applies if provided object id is non leaf entity such as Tag or a folder. This can be used to ignore specific objects under a parent object which has been included for protection. | [optional] 
**cdp_info** | [**VmwareCdpObject**](VmwareCdpObject.md) |  | [optional] 
**standby_info** | [**VmwareStandbyObject**](VmwareStandbyObject.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


