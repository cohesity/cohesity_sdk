# FirewallIPSet

Specifies a firewall IP set information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the name of the IP set. | 
**subnets** | **List[str]** | Specifies the subnets in the IP set. | 

## Example

```python
from cohesity_sdk.helios.models.firewall_ip_set import FirewallIPSet

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallIPSet from a JSON string
firewall_ip_set_instance = FirewallIPSet.from_json(json)
# print the JSON string representation of the object
print(FirewallIPSet.to_json())

# convert the object into a dict
firewall_ip_set_dict = firewall_ip_set_instance.to_dict()
# create an instance of FirewallIPSet from a dict
firewall_ip_set_from_dict = FirewallIPSet.from_dict(firewall_ip_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


