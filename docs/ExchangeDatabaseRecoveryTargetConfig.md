# ExchangeDatabaseRecoveryTargetConfig

Specifies the target object parameters to recover Exchange database.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.models.exchange_database_recovery_target_config import ExchangeDatabaseRecoveryTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeDatabaseRecoveryTargetConfig from a JSON string
exchange_database_recovery_target_config_instance = ExchangeDatabaseRecoveryTargetConfig.from_json(json)
# print the JSON string representation of the object
print(ExchangeDatabaseRecoveryTargetConfig.to_json())

# convert the object into a dict
exchange_database_recovery_target_config_dict = exchange_database_recovery_target_config_instance.to_dict()
# create an instance of ExchangeDatabaseRecoveryTargetConfig from a dict
exchange_database_recovery_target_config_from_dict = ExchangeDatabaseRecoveryTargetConfig.from_dict(exchange_database_recovery_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


