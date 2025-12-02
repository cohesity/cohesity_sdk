# SupportMfaConfigInfo

Holds the MFA configuration to be returned or stored.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from cohesity_sdk.cluster.models.support_mfa_config_info import SupportMfaConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SupportMfaConfigInfo from a JSON string
support_mfa_config_info_instance = SupportMfaConfigInfo.from_json(json)
# print the JSON string representation of the object
print(SupportMfaConfigInfo.to_json())

# convert the object into a dict
support_mfa_config_info_dict = support_mfa_config_info_instance.to_dict()
# create an instance of SupportMfaConfigInfo from a dict
support_mfa_config_info_from_dict = SupportMfaConfigInfo.from_dict(support_mfa_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


