# RecoverOracleAppNewSourceConfig

Specifies the new destination Source configuration where the databases will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**recover_database_params** | [**CommonOracleAppSourceConfig**](CommonOracleAppSourceConfig.md) |  | [optional] 
**recover_view_params** | [**CommonOracleAppSourceConfig**](CommonOracleAppSourceConfig.md) |  | [optional] 
**recovery_target** | **str** | Specifies if recovery target is a database or a view. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_oracle_app_new_source_config import RecoverOracleAppNewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverOracleAppNewSourceConfig from a JSON string
recover_oracle_app_new_source_config_instance = RecoverOracleAppNewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverOracleAppNewSourceConfig.to_json())

# convert the object into a dict
recover_oracle_app_new_source_config_dict = recover_oracle_app_new_source_config_instance.to_dict()
# create an instance of RecoverOracleAppNewSourceConfig from a dict
recover_oracle_app_new_source_config_from_dict = RecoverOracleAppNewSourceConfig.from_dict(recover_oracle_app_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


