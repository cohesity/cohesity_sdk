# RecoverOracleAppParams

Specifies the parameters to recover Oracle databases.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oracle_target_params** | [**CommonRecoverOracleAppTargetParams**](CommonRecoverOracleAppTargetParams.md) |  | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.recover_oracle_app_params import RecoverOracleAppParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverOracleAppParams from a JSON string
recover_oracle_app_params_instance = RecoverOracleAppParams.from_json(json)
# print the JSON string representation of the object
print(RecoverOracleAppParams.to_json())

# convert the object into a dict
recover_oracle_app_params_dict = recover_oracle_app_params_instance.to_dict()
# create an instance of RecoverOracleAppParams from a dict
recover_oracle_app_params_from_dict = RecoverOracleAppParams.from_dict(recover_oracle_app_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


