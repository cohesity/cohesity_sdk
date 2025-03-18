# CommonRecoverOracleAppTargetParams

Specifies the snapshot parameters to recover Oracle databases.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverOracleAppNewSourceConfig**](RecoverOracleAppNewSourceConfig.md) |  | [optional] 
**original_source_config** | [**CommonOracleAppSourceConfig**](CommonOracleAppSourceConfig.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new source or an original Source Target. | 

## Example

```python
from cohesity_sdk.cluster.models.common_recover_oracle_app_target_params import CommonRecoverOracleAppTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonRecoverOracleAppTargetParams from a JSON string
common_recover_oracle_app_target_params_instance = CommonRecoverOracleAppTargetParams.from_json(json)
# print the JSON string representation of the object
print(CommonRecoverOracleAppTargetParams.to_json())

# convert the object into a dict
common_recover_oracle_app_target_params_dict = common_recover_oracle_app_target_params_instance.to_dict()
# create an instance of CommonRecoverOracleAppTargetParams from a dict
common_recover_oracle_app_target_params_from_dict = CommonRecoverOracleAppTargetParams.from_dict(common_recover_oracle_app_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


