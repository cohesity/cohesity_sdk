# HyperVObjectProtectionRequest

Specifies the HyperV object level settings for object protection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | Specifies the id of the object being protected. This can be a leaf level or non leaf level object. | 
**exclude_object_ids** | **[int, none_type]** | Specifies the list of IDs of the objects to not be protected by this Protection Group. This can be used to ignore specific objects under a parent object which has been included for protection. | [optional] 
**backups_copy_only** | **bool, none_type** | Specifies whether the backups should be copy-only. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


