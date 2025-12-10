# MfaParams

Specifies the multi-factor authentication params.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**otp_code** | **str** | Specifies OTP code for MFA verification. | [optional] 
**otp_type** | **str** | Specifies the list of mechanism to receive the OTP code. Supported types are: TOTP (Helios OnPrem Only) -&gt; Time based OTP. Email OTP (Helios OnPrem Only) -&gt; OTP via Email. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.mfa_params import MfaParams

# TODO update the JSON string below
json = "{}"
# create an instance of MfaParams from a JSON string
mfa_params_instance = MfaParams.from_json(json)
# print the JSON string representation of the object
print(MfaParams.to_json())

# convert the object into a dict
mfa_params_dict = mfa_params_instance.to_dict()
# create an instance of MfaParams from a dict
mfa_params_from_dict = MfaParams.from_dict(mfa_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


