# VmwareObjectProtectionResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cdp_info** | [**VmwareCdpObject**](VmwareCdpObject.md) |  | [optional] 
**exclude_object_ids** | **[int, none_type]** | Specifies the list of IDs of the objects to not be protected in this backup. This field only applies if provided object id is non leaf entity such as Tag or a folder. This can be used to ignore specific objects under a parent object which has been included for protection. | [optional] 
**standby_info** | [**VmwareStandbyObject**](VmwareStandbyObject.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


