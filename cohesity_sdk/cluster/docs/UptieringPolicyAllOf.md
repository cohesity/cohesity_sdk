# UptieringPolicyAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_age** | [**UptieringFileAgePolicy**](UptieringFileAgePolicy.md) |  | [optional] 
**include_all_files** | **bool, none_type** | If set, all files in the view will be uptiered regardless of file_select_policy, num_file_access, hot_file_window, file_size constraints. | [optional]  if omitted the server will use the default value of False
**target** | [**UptieringTarget**](UptieringTarget.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


