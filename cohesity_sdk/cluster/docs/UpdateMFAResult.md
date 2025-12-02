# UpdateMFAResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_name** | **str** | Specifies the TOTP account name to be configured for support user. | [optional] 
**totp_secret_key** | **str** | Specifies the TOTP secret key. | [optional] 
**totp_uri** | **str** | Specifies the TOTP key URI for generating MFA QR code. | [optional] 
**current_password** | **str** | Specifies the current password of the support user, required for making updates to the configuration. | [optional] 
**email** | **str** | This field is deprecated, use PUT /v2/support-user/mfa. Specifies email address of the support user. Used when MFA mode is email. | [optional] 
**enabled** | **bool** | Specifies whether MFA is enabled for support user. | [optional] [default to False]
**is_quorum_managed** | **bool** | Specifies whether the MFA configuration is managed by quorum. | [optional] [readonly] [default to False]
**mfa_code** | **str** | MFA code that needs to be passed when disabling MFA or changing email address when email based MFA is configured. | [optional] 
**mfa_type** | **str** | This field is deprecated, use PUT /v2/support-user/mfa. Specifies the mechanism to receive the OTP code. | [optional] 
**otp_verification_state** | **str** | Specifies the status of otp verification. | [optional] 
**reference_id** | **str** | Specifies a reference ID of OTP verification, required if mfaCode is not specified | [optional] 
**requires_password_auth** | **bool** | Specifies that this API requires current support user password for enabling/disabling MFA, and for updating mfaType and email. | [optional] [readonly] [default to True]

## Example

```python
from cohesity_sdk.cluster.models.update_mfa_result import UpdateMFAResult

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMFAResult from a JSON string
update_mfa_result_instance = UpdateMFAResult.from_json(json)
# print the JSON string representation of the object
print(UpdateMFAResult.to_json())

# convert the object into a dict
update_mfa_result_dict = update_mfa_result_instance.to_dict()
# create an instance of UpdateMFAResult from a dict
update_mfa_result_from_dict = UpdateMFAResult.from_dict(update_mfa_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


