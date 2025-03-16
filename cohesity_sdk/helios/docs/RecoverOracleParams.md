# RecoverOracleParams

Specifies the recovery options specific to oracle environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[RecoverOracleDbSnapshotParams]**](RecoverOracleDbSnapshotParams.md) | Specifies the list of parameters for list of objects to be recovered. | 
**recover_app_params** | [**RecoverOracleAppParams**](RecoverOracleAppParams.md) | Specifies the parameters to recover Oracle databases. | [optional] 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 

## Example

```python
from cohesity_sdk.helios.models.recover_oracle_params import RecoverOracleParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverOracleParams from a JSON string
recover_oracle_params_instance = RecoverOracleParams.from_json(json)
# print the JSON string representation of the object
print(RecoverOracleParams.to_json())

# convert the object into a dict
recover_oracle_params_dict = recover_oracle_params_instance.to_dict()
# create an instance of RecoverOracleParams from a dict
recover_oracle_params_from_dict = RecoverOracleParams.from_dict(recover_oracle_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


