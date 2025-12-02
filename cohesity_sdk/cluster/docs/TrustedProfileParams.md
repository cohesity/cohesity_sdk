# TrustedProfileParams

Specifies the trusted profile authentication method parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trusted_profile_id** | **str** | Specifies ID of the trusted profile. | 

## Example

```python
from cohesity_sdk.cluster.models.trusted_profile_params import TrustedProfileParams

# TODO update the JSON string below
json = "{}"
# create an instance of TrustedProfileParams from a JSON string
trusted_profile_params_instance = TrustedProfileParams.from_json(json)
# print the JSON string representation of the object
print(TrustedProfileParams.to_json())

# convert the object into a dict
trusted_profile_params_dict = trusted_profile_params_instance.to_dict()
# create an instance of TrustedProfileParams from a dict
trusted_profile_params_from_dict = TrustedProfileParams.from_dict(trusted_profile_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


