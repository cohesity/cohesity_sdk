# NTPSettings

Specifies if the ntp/primary secondary scheme should be disabled

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ntp_authentication_enabled** | **bool** | Specifies if the cluster is using NTP with authentication. | [optional] 
**ntp_servers_internal** | **bool** | Specifies if the NTP servers are on internal network or not. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.ntp_settings import NTPSettings

# TODO update the JSON string below
json = "{}"
# create an instance of NTPSettings from a JSON string
ntp_settings_instance = NTPSettings.from_json(json)
# print the JSON string representation of the object
print(NTPSettings.to_json())

# convert the object into a dict
ntp_settings_dict = ntp_settings_instance.to_dict()
# create an instance of NTPSettings from a dict
ntp_settings_from_dict = NTPSettings.from_dict(ntp_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


