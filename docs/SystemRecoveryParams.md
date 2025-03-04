# SystemRecoveryParams

Specifies the parameters to perform a system recovery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_nas_path** | **str** | Specifies the path to the recovery view. | [optional] 

## Example

```python
from cohesity_sdk.models.system_recovery_params import SystemRecoveryParams

# TODO update the JSON string below
json = "{}"
# create an instance of SystemRecoveryParams from a JSON string
system_recovery_params_instance = SystemRecoveryParams.from_json(json)
# print the JSON string representation of the object
print(SystemRecoveryParams.to_json())

# convert the object into a dict
system_recovery_params_dict = system_recovery_params_instance.to_dict()
# create an instance of SystemRecoveryParams from a dict
system_recovery_params_from_dict = SystemRecoveryParams.from_dict(system_recovery_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


