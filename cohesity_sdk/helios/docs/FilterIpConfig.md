# FilterIpConfig

Specifies the list of IP addresses that are allowed or denied during recovery. Allowed IPs and Denied IPs cannot be used together.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_ip_addresses** | **List[str]** | Specifies the IP addresses that should be used exclusively during recovery. Cannot be set if deniedIpAddresses is set. | [optional] 
**denied_ip_addresses** | **List[str]** | Specifies the IP addresses that should not be used during recovery recovery. Cannot be set if allowedIpAddresses is set. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.filter_ip_config import FilterIpConfig

# TODO update the JSON string below
json = "{}"
# create an instance of FilterIpConfig from a JSON string
filter_ip_config_instance = FilterIpConfig.from_json(json)
# print the JSON string representation of the object
print(FilterIpConfig.to_json())

# convert the object into a dict
filter_ip_config_dict = filter_ip_config_instance.to_dict()
# create an instance of FilterIpConfig from a dict
filter_ip_config_from_dict = FilterIpConfig.from_dict(filter_ip_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


