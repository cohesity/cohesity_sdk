# AzureTargetParamsForRecoverAzureBlobStorage

Specifies the recovery target params for Azure Blob Storage target config.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_to_new_source** | **bool, none_type** | Specifies the parameter whether the recovery should be performed to a new or an existing target. | 
**continue_on_error** | **bool, none_type** | Specifies whether to continue restore on receiving error or not. Default is true. | [optional] 
**new_source_config** | [**RecoverAzureBlobStorageNewSourceConfig**](RecoverAzureBlobStorageNewSourceConfig.md) |  | [optional] 
**object_prefix** | **str, none_type** | Specifies the prefix to be added to all the objects being recovered. | [optional] 
**overwrite_existing** | **bool, none_type** | Specifies whether to override the existing objects. Default is false. | [optional] 
**preserve_object_attributes** | **bool, none_type** | Specifies if we should preserve object attributes at the time of restore. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


