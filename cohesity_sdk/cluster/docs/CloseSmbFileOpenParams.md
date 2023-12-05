# CloseSmbFileOpenParams

Specifies params to close active SMB file open.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_path** | **str, none_type** | Specifies the filepath in the Cohesity View relative to the root filesystem. If this field is specified, viewName field must also be specified. | 
**open_id** | **int, none_type** | Specifies the id of the active open. | 
**view_name** | **str, none_type** | Specifies the name of the Cohesity View in which to search. If a view name is not specified, all the views in the Cluster are searched. This field is mandatory if filePath field is specified. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


