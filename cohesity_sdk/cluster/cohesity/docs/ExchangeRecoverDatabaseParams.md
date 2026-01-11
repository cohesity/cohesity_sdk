# ExchangeRecoverDatabaseParams

Specifies the parameters to recover an Exchange database. database.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing Source Target. | 
**restore_type** | **str, none_type** | Specifies the type of exchange restore. | defaults to "RestoreView"
**recovery_target_config** | [**ExchangeDatabaseRecoveryTargetConfig**](ExchangeDatabaseRecoveryTargetConfig.md) |  | [optional] 
**view_options** | [**ViewOptions**](ViewOptions.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


