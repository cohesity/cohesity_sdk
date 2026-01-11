# GCPTargetParamsForRecoverGCPSqlServer

Specifies the recovery target params for Google SQL Server target config.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing target. | 
**cloud_storage_bucket_name** | **str** | The Google Cloud Storage bucket name for SQL recovery. | [optional] 
**new_source_config** | [**RecoverGCPSqlServerNewSourceConfig**](RecoverGCPSqlServerNewSourceConfig.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


