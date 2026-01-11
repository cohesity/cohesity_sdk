# RdsMsSQLRecoveryTargetConfig

Specifies the target object parameters to recover AWS RDS MS SQL.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing Source Target. | 
**bucket_auto_create** | **bool, none_type** | Specifies whether to auto create the Cloud Storage bucket if it does not exist. | [optional] 
**cloud_storage_bucket_name** | **str, none_type** | The Cloud Storage bucket name for MS SQL database recovery. | [optional] 
**new_source_config** | [**RecoverRdsMsSQLNewSourceConfig**](RecoverRdsMsSQLNewSourceConfig.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


