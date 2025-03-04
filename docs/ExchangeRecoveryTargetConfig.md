# ExchangeRecoveryTargetConfig

Specifies the target object parameters to recover an Exchange database.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_directory_location** | **str** | Specifies the directory where to put the database data files. Missing directory will be automatically created. | [optional] 
**database_name** | **str** | Specifies a new name for the restored database. | [optional] 
**log_directory_location** | **str** | Specifies the directory where to put the database log files. Missing directory will be automatically created. | [optional] 
**mount_database** | **bool** | Specifies whether to mount the database after successful recovery. | [optional] 
**restore_as_recovery_db** | **bool** | Specifies whether to restore the Database as Recovery database. | [optional] 
**roll_forward_recovery** | **bool** | Specifies whether to use the latest logs on Exchange Server to perform roll-forward recovery. | [optional] 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.exchange_recovery_target_config import ExchangeRecoveryTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeRecoveryTargetConfig from a JSON string
exchange_recovery_target_config_instance = ExchangeRecoveryTargetConfig.from_json(json)
# print the JSON string representation of the object
print(ExchangeRecoveryTargetConfig.to_json())

# convert the object into a dict
exchange_recovery_target_config_dict = exchange_recovery_target_config_instance.to_dict()
# create an instance of ExchangeRecoveryTargetConfig from a dict
exchange_recovery_target_config_from_dict = ExchangeRecoveryTargetConfig.from_dict(exchange_recovery_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


