# DnsServersInfo

List of DNS servers in cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_servers** | **List[str]** | List of DNS servers in cluster. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.dns_servers_info import DnsServersInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DnsServersInfo from a JSON string
dns_servers_info_instance = DnsServersInfo.from_json(json)
# print the JSON string representation of the object
print(DnsServersInfo.to_json())

# convert the object into a dict
dns_servers_info_dict = dns_servers_info_instance.to_dict()
# create an instance of DnsServersInfo from a dict
dns_servers_info_from_dict = DnsServersInfo.from_dict(dns_servers_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


