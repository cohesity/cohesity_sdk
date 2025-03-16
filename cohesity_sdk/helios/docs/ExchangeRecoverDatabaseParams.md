# ExchangeRecoverDatabaseParams

Specifies the parameters to recover an Exchange database. database.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the source id of Exchange database which has to be recovered. | 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing Source Target. | 
**recovery_target_config** | [**ExchangeDatabaseRecoveryTargetConfig**](ExchangeDatabaseRecoveryTargetConfig.md) | Specifies the recovery target configuration if recovery has to be done to a different location which is different from original source. | [optional] 
**restore_type** | **str** | Specifies the type of exchange restore. | 
**view_options** | [**ViewOptions**](ViewOptions.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.exchange_recover_database_params import ExchangeRecoverDatabaseParams

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeRecoverDatabaseParams from a JSON string
exchange_recover_database_params_instance = ExchangeRecoverDatabaseParams.from_json(json)
# print the JSON string representation of the object
print(ExchangeRecoverDatabaseParams.to_json())

# convert the object into a dict
exchange_recover_database_params_dict = exchange_recover_database_params_instance.to_dict()
# create an instance of ExchangeRecoverDatabaseParams from a dict
exchange_recover_database_params_from_dict = ExchangeRecoverDatabaseParams.from_dict(exchange_recover_database_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


