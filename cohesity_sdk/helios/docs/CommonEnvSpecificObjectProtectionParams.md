# CommonEnvSpecificObjectProtectionParams

Specifies common properties of Object Protection Operations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | Specifies the environment for current object. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.common_env_specific_object_protection_params import CommonEnvSpecificObjectProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonEnvSpecificObjectProtectionParams from a JSON string
common_env_specific_object_protection_params_instance = CommonEnvSpecificObjectProtectionParams.from_json(json)
# print the JSON string representation of the object
print(CommonEnvSpecificObjectProtectionParams.to_json())

# convert the object into a dict
common_env_specific_object_protection_params_dict = common_env_specific_object_protection_params_instance.to_dict()
# create an instance of CommonEnvSpecificObjectProtectionParams from a dict
common_env_specific_object_protection_params_from_dict = CommonEnvSpecificObjectProtectionParams.from_dict(common_env_specific_object_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


