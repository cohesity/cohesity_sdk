# UserMfaInfo

Specifies the Multi-factor Authentication (MFA) information for the user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_mfa_exempt** | **bool** | Specifies if the user is exempted from MFA. | [optional] 
**is_totp_setup_done** | **bool** | Specifies if the Time-Based One-Time Password (TOTP) setup was done for the user MFA. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.user_mfa_info import UserMfaInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UserMfaInfo from a JSON string
user_mfa_info_instance = UserMfaInfo.from_json(json)
# print the JSON string representation of the object
print(UserMfaInfo.to_json())

# convert the object into a dict
user_mfa_info_dict = user_mfa_info_instance.to_dict()
# create an instance of UserMfaInfo from a dict
user_mfa_info_from_dict = UserMfaInfo.from_dict(user_mfa_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


