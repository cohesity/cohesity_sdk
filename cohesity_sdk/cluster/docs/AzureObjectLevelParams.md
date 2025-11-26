# AzureObjectLevelParams

Specifies the Azure object level settings for object protection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | Specifies the id of the object being protected. This can be a leaf level or non leaf level object. | 
**disk_exclusion_params** | [**AzureDiskExclusionParams**](AzureDiskExclusionParams.md) |  | [optional] 
**exclude_object_ids** | **[int, none_type]** | Specifies the list of IDs of the objects not to be protected in this backup. This field only applies if provided object id is non leaf entity such as Tag. This can be used to ignore specific objects (can include tags) under a parent object which has been included for protection. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


