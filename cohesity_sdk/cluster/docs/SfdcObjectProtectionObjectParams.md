# SfdcObjectProtectionObjectParams

Specifies the object parameters to create an Sfdc Object Protection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the Sfdc Org being protected. This cannot be the id of a leaf level object. By default, the Sfdc Org is auto-protected. | 
**exclude_object_ids** | **[int], none_type** | Specifies the ids of the objects to be excluded in the Object Protection. | [optional] 
**field_exclusion_list** | [**[SfdcObjectFieldExclusion], none_type**](SfdcObjectFieldExclusion.md) | Specifies the list of field names to be excluded in an Sfdc object. A user can specify multiple such entries in this list. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


