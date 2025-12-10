# ConfigureSupportUserMfaParams

Specifies the request parameters for updating support user MFA configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_password** | **str** | Specifies the current password of the support user, required for making updates to the configuration. | [optional] 
**email** | **str** | Specifies email address of the support user. Required when the support user email is being modified. | [optional] 
**mfa_type** | **str** | Specifies the mechanism to receive the OTP code. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.configure_support_user_mfa_params import ConfigureSupportUserMfaParams

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigureSupportUserMfaParams from a JSON string
configure_support_user_mfa_params_instance = ConfigureSupportUserMfaParams.from_json(json)
# print the JSON string representation of the object
print(ConfigureSupportUserMfaParams.to_json())

# convert the object into a dict
configure_support_user_mfa_params_dict = configure_support_user_mfa_params_instance.to_dict()
# create an instance of ConfigureSupportUserMfaParams from a dict
configure_support_user_mfa_params_from_dict = ConfigureSupportUserMfaParams.from_dict(configure_support_user_mfa_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


