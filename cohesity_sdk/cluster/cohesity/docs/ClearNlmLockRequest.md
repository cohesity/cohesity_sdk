# ClearNlmLockRequest

Specifies details required to clear NLM lock.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Specifies the id of the client, related to which NLM locks needs to be clear. | [optional] 
**file_path** | **str** | Specifies the filepath in the view relative to the root filesystem. If this field is specified, viewName field must also be specified. | [optional] 
**view_name** | **str** | Specifies the name of the View in which to search. If a view name is not specified, all the views in the Cluster are searched. This field is mandatory if filePath field is specified. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


