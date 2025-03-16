# CreateAuthenticatorKeyBaseResponse

Specifies the response for initiating MFA Key code setup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticator_type** | **str** | Type of Auth mechanism to use for sending MFA OTP. | 

## Example

```python
from cohesity_sdk.helios.models.create_authenticator_key_base_response import CreateAuthenticatorKeyBaseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuthenticatorKeyBaseResponse from a JSON string
create_authenticator_key_base_response_instance = CreateAuthenticatorKeyBaseResponse.from_json(json)
# print the JSON string representation of the object
print(CreateAuthenticatorKeyBaseResponse.to_json())

# convert the object into a dict
create_authenticator_key_base_response_dict = create_authenticator_key_base_response_instance.to_dict()
# create an instance of CreateAuthenticatorKeyBaseResponse from a dict
create_authenticator_key_base_response_from_dict = CreateAuthenticatorKeyBaseResponse.from_dict(create_authenticator_key_base_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


