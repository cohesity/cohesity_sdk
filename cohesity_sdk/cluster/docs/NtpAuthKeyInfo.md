# NtpAuthKeyInfo

Specifies list of authentication keys corresponding to each NTP server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ntp_server_address** | **str** | Specifies NTP server address. | [optional] 
**ntp_server_auth_key_encryption_algorithm** | **str** | Specifies the Symmetric Key algorithm used for the encryption key. | [optional] 
**ntp_server_auth_key_id** | **int** | Specifies the identifier of the authentication key used to verify the NTP server. | [optional] 
**ntp_server_auth_key_value** | **str** | Specifies the shared secret key corresponding to the authentication key identifier used to authenticate NTP messages. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.ntp_auth_key_info import NtpAuthKeyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NtpAuthKeyInfo from a JSON string
ntp_auth_key_info_instance = NtpAuthKeyInfo.from_json(json)
# print the JSON string representation of the object
print(NtpAuthKeyInfo.to_json())

# convert the object into a dict
ntp_auth_key_info_dict = ntp_auth_key_info_instance.to_dict()
# create an instance of NtpAuthKeyInfo from a dict
ntp_auth_key_info_from_dict = NtpAuthKeyInfo.from_dict(ntp_auth_key_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


