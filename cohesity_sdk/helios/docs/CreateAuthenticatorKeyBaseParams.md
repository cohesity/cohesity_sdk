# CreateAuthenticatorKeyBaseParams

Specifies the input params for initiating MFA Key code setup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticator_type** | **str** | Type of Auth mechanism to use for sending MFA OTP. | 

## Example

```python
from cohesity_sdk.helios.models.create_authenticator_key_base_params import CreateAuthenticatorKeyBaseParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuthenticatorKeyBaseParams from a JSON string
create_authenticator_key_base_params_instance = CreateAuthenticatorKeyBaseParams.from_json(json)
# print the JSON string representation of the object
print(CreateAuthenticatorKeyBaseParams.to_json())

# convert the object into a dict
create_authenticator_key_base_params_dict = create_authenticator_key_base_params_instance.to_dict()
# create an instance of CreateAuthenticatorKeyBaseParams from a dict
create_authenticator_key_base_params_from_dict = CreateAuthenticatorKeyBaseParams.from_dict(create_authenticator_key_base_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


