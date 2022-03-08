# UptieringPolicy

Specifies the data uptiering policy.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_age** | [**UptieringFileAgePolicy**](UptieringFileAgePolicy.md) |  | [optional] 
**include_all_files** | **bool, none_type** | If set, all files in the view will be uptiered regardless of file_select_policy, num_file_access, hot_file_window, file_size constraints. | [optional]  if omitted the server will use the default value of False
**target** | [**UptieringTarget**](UptieringTarget.md) |  | [optional] 
**enable_audit_logging** | **bool, none_type** | Specifies whether to audit log the file tiering activity. | [optional]  if omitted the server will use the default value of False
**file_size** | [**FileSizePolicy**](FileSizePolicy.md) |  | [optional] 
**file_path** | [**FileFilteringPolicy**](FileFilteringPolicy.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


