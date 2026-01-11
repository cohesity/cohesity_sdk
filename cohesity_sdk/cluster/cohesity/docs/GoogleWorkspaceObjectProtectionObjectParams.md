# GoogleWorkspaceObjectProtectionObjectParams

Specifies the object parameters to create a Google Workspace Object Protection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the object being protected. If this is a non leaf level object, then the object will be auto-protected unless leaf objects are specified for exclusion. | 
**exclude_object_ids** | **[int], none_type** | Specifies the ID of the objects to be excluded in the Object Protection. | [optional] 
**name** | **str, none_type** | Specifies the name of the object. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


