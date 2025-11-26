# Office365ObjectProtectionObjectParams

Specifies the object parameters to create a Microsoft 365 Object Protection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the object being protected. If this is a non leaf level object, then the object will be auto-protected unless leaf objects are specified for exclusion. | 
**exclude_object_ids** | **[int], none_type** | Specifies the ID of the objects to be excluded in the Object Protection. | [optional] 
**name** | **str, none_type** | Specifies the name of the object. | [optional] [readonly] 
**should_auto_protect_object** | **bool, none_type** | Specifies if the object has to be autoprotected. This is applicable only for sharepoint sites. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


