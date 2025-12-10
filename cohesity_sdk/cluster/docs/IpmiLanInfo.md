# IpmiLanInfo

Specifies the lan info for the ipmi.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **int** | Specifies the channel through which the IPMI interface communicates on the network. | [optional] 
**default_gateway_ip** | **str** | Specifies the default gateway ip for the given ipmi lan. | [optional] 
**default_gateway_mac** | **str** | Specifies the default gateway mac address for the given ipmi lan. | [optional] 
**ip_addr_source** | **str** | Specifies the ipmi lan address source. | [optional] 
**lan_ip** | **str** | Specifies the ip address for the given ipmi lan. | [optional] 
**subnet_mask** | **str** | Specifies the subnet mask for the given ipmi lan. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.ipmi_lan_info import IpmiLanInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IpmiLanInfo from a JSON string
ipmi_lan_info_instance = IpmiLanInfo.from_json(json)
# print the JSON string representation of the object
print(IpmiLanInfo.to_json())

# convert the object into a dict
ipmi_lan_info_dict = ipmi_lan_info_instance.to_dict()
# create an instance of IpmiLanInfo from a dict
ipmi_lan_info_from_dict = IpmiLanInfo.from_dict(ipmi_lan_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


