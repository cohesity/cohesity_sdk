# RecoverExchangeDbsParams

Specifies the parameters to recover Exchange databases.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing target. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | defaults to "kExchange"
**exchange_target_params** | [**ExchangeTargetParamsForRecoverExchangeDbs**](ExchangeTargetParamsForRecoverExchangeDbs.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


