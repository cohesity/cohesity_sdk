# CommonTieringPolicy

Specifies the common tiering params between uptiering and downtiering.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_audit_logging** | **bool, none_type** | Specifies whether to audit log the file tiering activity. | [optional]  if omitted the server will use the default value of False
**file_path** | [**FileFilteringPolicy**](FileFilteringPolicy.md) |  | [optional] 
**file_size** | [**FileSizePolicy**](FileSizePolicy.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


