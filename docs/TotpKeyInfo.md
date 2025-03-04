# TotpKeyInfo

Specifies the Time based OTP key info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**totp_key_id** | **str** | Specifies the Time based OTP key ID. | [optional] 
**totp_key_name** | **str** | Specifies the Time based OTP key name. | [optional] 
**totp_secret_key** | **str** | Specifies the Time based OTP secret key. | [optional] 
**totp_uri** | **str** | Specifies the Time based OTP key URI for generating MFA QR code. | [optional] 

## Example

```python
from cohesity_sdk.models.totp_key_info import TotpKeyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TotpKeyInfo from a JSON string
totp_key_info_instance = TotpKeyInfo.from_json(json)
# print the JSON string representation of the object
print(TotpKeyInfo.to_json())

# convert the object into a dict
totp_key_info_dict = totp_key_info_instance.to_dict()
# create an instance of TotpKeyInfo from a dict
totp_key_info_from_dict = TotpKeyInfo.from_dict(totp_key_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


