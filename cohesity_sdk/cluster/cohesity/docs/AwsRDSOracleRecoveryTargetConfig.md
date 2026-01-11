# AwsRDSOracleRecoveryTargetConfig

Specifies the target object parameters to recover AWS RDS Oracle.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverAwsRDSOracleNewSourceConfig**](RecoverAwsRDSOracleNewSourceConfig.md) |  | 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing Source Target. | 
**num_channels** | **int, none_type** | Number of channels for Oracle restore. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


