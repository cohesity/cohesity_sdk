# ExchangeRecoverDatabaseParams

Specifies the parameters to recover an Exchange database. database.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_source** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the source id of Exchange database which has to be recovered. | 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing Source Target. | 
**restore_type** | **str, none_type** | Specifies the type of exchange restore. | defaults to "RestoreView"
**recovery_target_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the recovery target configuration if recovery has to be done to a different location which is different from original source. | [optional] 
**view_options** | [**ViewOptions**](ViewOptions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


