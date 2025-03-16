# CreateAuthenticatorKeyBody

Specifies the input params for initiating MFA Key code setup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticator_type** | **str** | Type of Auth mechanism to use for sending MFA OTP. | 
**email_params** | **object** | No Content | [optional] 
**totp_params** | [**CreateTotpKeyRequestBody**](CreateTotpKeyRequestBody.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.create_authenticator_key_body import CreateAuthenticatorKeyBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuthenticatorKeyBody from a JSON string
create_authenticator_key_body_instance = CreateAuthenticatorKeyBody.from_json(json)
# print the JSON string representation of the object
print(CreateAuthenticatorKeyBody.to_json())

# convert the object into a dict
create_authenticator_key_body_dict = create_authenticator_key_body_instance.to_dict()
# create an instance of CreateAuthenticatorKeyBody from a dict
create_authenticator_key_body_from_dict = CreateAuthenticatorKeyBody.from_dict(create_authenticator_key_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


