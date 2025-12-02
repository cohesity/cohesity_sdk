# MfaConfigInfo

Holds the MFA configuration to be returned or stored.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_types** | **List[str]** | Specifies the list of mechanism to receive the OTP code. | [optional] 
**enabled** | **bool** | Specifies whether MFA is enabled on a cluster level. | [optional] [default to False]
**retain_user_mfa_settings** | **bool** | Specifies whether user MFA setting needs to be retained. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.mfa_config_info import MfaConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MfaConfigInfo from a JSON string
mfa_config_info_instance = MfaConfigInfo.from_json(json)
# print the JSON string representation of the object
print(MfaConfigInfo.to_json())

# convert the object into a dict
mfa_config_info_dict = mfa_config_info_instance.to_dict()
# create an instance of MfaConfigInfo from a dict
mfa_config_info_from_dict = MfaConfigInfo.from_dict(mfa_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


