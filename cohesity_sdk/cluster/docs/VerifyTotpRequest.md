# VerifyTotpRequest

Holds the Totp code to be verified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purpose** | **str** | Specifies the purpose of the totp code verification. * &#x60;DisableMfa&#x60; - To be used when disabling the MFA. * &#x60;VerifyOtp&#x60; (Default) - To be used when verifying OTP. | [optional] 
**support_user_password** | **str** | Specifies the support user password, required for totp verification while disabling MFA. | [optional] 
**totp_code** | **str** | Specifies the Totp code. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.verify_totp_request import VerifyTotpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyTotpRequest from a JSON string
verify_totp_request_instance = VerifyTotpRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyTotpRequest.to_json())

# convert the object into a dict
verify_totp_request_dict = verify_totp_request_instance.to_dict()
# create an instance of VerifyTotpRequest from a dict
verify_totp_request_from_dict = VerifyTotpRequest.from_dict(verify_totp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


