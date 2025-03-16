# OracleTargetParamsForRecoverOracleApp

Specifies the params for recovering to a oracle host. Provided oracle backup should be recovered to same type of target host. For Example: If you have oracle backup taken from a physical host then that should be recovered to physical host only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverOracleAppNewSourceConfig**](RecoverOracleAppNewSourceConfig.md) | Specifies the destination Source configuration parameters where the databases will be recovered. This is mandatory if recoverToNewSource is set to true. | [optional] 
**original_source_config** | [**RecoverOracleAppOriginalSourceConfig**](RecoverOracleAppOriginalSourceConfig.md) | Specifies the Source configuration if databases are being recovered to Original Source. If not specified, all the configuration parameters will be retained. | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new source or an original Source Target. | 

## Example

```python
from cohesity_sdk.helios.models.oracle_target_params_for_recover_oracle_app import OracleTargetParamsForRecoverOracleApp

# TODO update the JSON string below
json = "{}"
# create an instance of OracleTargetParamsForRecoverOracleApp from a JSON string
oracle_target_params_for_recover_oracle_app_instance = OracleTargetParamsForRecoverOracleApp.from_json(json)
# print the JSON string representation of the object
print(OracleTargetParamsForRecoverOracleApp.to_json())

# convert the object into a dict
oracle_target_params_for_recover_oracle_app_dict = oracle_target_params_for_recover_oracle_app_instance.to_dict()
# create an instance of OracleTargetParamsForRecoverOracleApp from a dict
oracle_target_params_for_recover_oracle_app_from_dict = OracleTargetParamsForRecoverOracleApp.from_dict(oracle_target_params_for_recover_oracle_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


