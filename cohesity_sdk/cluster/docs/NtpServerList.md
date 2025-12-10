# NtpServerList

Specifies the list of NTP servers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ntp_authentication_enabled** | **bool** | Specifies whether NTP servers use authentication. | [optional] 
**ntp_server_auth_info** | [**List[NtpAuthKeyInfo]**](NtpAuthKeyInfo.md) | Specifies list of NTP authentication keys. | [optional] 
**ntp_servers** | **List[str]** | Specifies list of NTP server addresses. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.ntp_server_list import NtpServerList

# TODO update the JSON string below
json = "{}"
# create an instance of NtpServerList from a JSON string
ntp_server_list_instance = NtpServerList.from_json(json)
# print the JSON string representation of the object
print(NtpServerList.to_json())

# convert the object into a dict
ntp_server_list_dict = ntp_server_list_instance.to_dict()
# create an instance of NtpServerList from a dict
ntp_server_list_from_dict = NtpServerList.from_dict(ntp_server_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


