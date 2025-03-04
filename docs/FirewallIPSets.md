# FirewallIPSets

Specifies the list of firewall IP sets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_sets** | [**List[FirewallIPSet]**](FirewallIPSet.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.firewall_ip_sets import FirewallIPSets

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallIPSets from a JSON string
firewall_ip_sets_instance = FirewallIPSets.from_json(json)
# print the JSON string representation of the object
print(FirewallIPSets.to_json())

# convert the object into a dict
firewall_ip_sets_dict = firewall_ip_sets_instance.to_dict()
# create an instance of FirewallIPSets from a dict
firewall_ip_sets_from_dict = FirewallIPSets.from_dict(firewall_ip_sets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


