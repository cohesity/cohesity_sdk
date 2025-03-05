# SupportTotpKeyInfo

Specifies the TOTP key info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_name** | **str** | Specifies the TOTP account name to be configured for support user. | [optional] 
**totp_secret_key** | **str** | Specifies the TOTP secret key. | [optional] 
**totp_uri** | **str** | Specifies the TOTP key URI for generating MFA QR code. | [optional] 

## Example

```python
from cohesity_sdk.models.support_totp_key_info import SupportTotpKeyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SupportTotpKeyInfo from a JSON string
support_totp_key_info_instance = SupportTotpKeyInfo.from_json(json)
# print the JSON string representation of the object
print(SupportTotpKeyInfo.to_json())

# convert the object into a dict
support_totp_key_info_dict = support_totp_key_info_instance.to_dict()
# create an instance of SupportTotpKeyInfo from a dict
support_totp_key_info_from_dict = SupportTotpKeyInfo.from_dict(support_totp_key_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


