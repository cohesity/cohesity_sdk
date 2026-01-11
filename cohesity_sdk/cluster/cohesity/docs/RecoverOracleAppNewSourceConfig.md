# RecoverOracleAppNewSourceConfig

Specifies the new destination Source configuration where the databases will be recovered.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**recover_database_params** | [**CommonOracleAppSourceConfig**](CommonOracleAppSourceConfig.md) |  | [optional] 
**recover_view_params** | [**CommonOracleAppSourceConfig**](CommonOracleAppSourceConfig.md) |  | [optional] 
**recovery_target** | **str, none_type** | Specifies if recovery target is a database or a view. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


