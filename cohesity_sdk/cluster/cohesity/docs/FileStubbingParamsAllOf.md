# FileStubbingParamsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_orphan_data_cleanup** | **bool, none_type** | Specifies whether to remove the orphan data from the target if the symlink is removed from the source. | [optional]  if omitted the server will use the default value of True
**downtiering_file_age** | [**DowntieringFileAgePolicy**](DowntieringFileAgePolicy.md) |  | [optional] 
**skip_back_symlink** | **bool, none_type** | Specifies whether to create a symlink for the migrated data from source to target. | [optional]  if omitted the server will use the default value of True
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


