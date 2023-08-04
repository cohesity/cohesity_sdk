# DowntieringPolicy

Specifies the data downtiering policy.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qos_policy** | **str, none_type** | Specifies whether the data tiering task will be written to HDD or SSD. | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**retention** | [**Retention**](Retention.md) |  | [optional] 
**skip_back_symlink** | **bool, none_type** | Specifies whether to create a symlink for the migrated data from source to target. | [optional]  if omitted the server will use the default value of True
**auto_orphan_data_cleanup** | **bool, none_type** | Specifies whether to remove the orphan data from the target if the symlink is removed from the source. | [optional]  if omitted the server will use the default value of True
**tiering_goal** | **int, none_type** | Specifies the maximum amount of data that should be present on source after downtiering. | [optional] 
**file_age** | [**DowntieringFileAgePolicy**](DowntieringFileAgePolicy.md) |  | [optional] 
**target** | [**DowntieringTarget**](DowntieringTarget.md) |  | [optional] 
**tags_info** | [**[DataTieringTagObject], none_type**](DataTieringTagObject.md) | Array of Tag objects used to represent different file based policies | [optional] 
**enable_audit_logging** | **bool, none_type** | Specifies whether to audit log the file tiering activity. | [optional]  if omitted the server will use the default value of False
**file_size** | [**FileSizePolicy**](FileSizePolicy.md) |  | [optional] 
**file_path** | [**FileFilteringPolicy**](FileFilteringPolicy.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


