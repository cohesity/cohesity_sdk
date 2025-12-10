# FirewallEntry

Specifies the firewall settings of a node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**List[Attachment]**](Attachment.md) | Specifies the firewall profile attachments. | [optional] 
**ipsets** | [**List[FirewallIPSet]**](FirewallIPSet.md) | Specifies the firewall ipsets. | [optional] 
**profiles** | [**List[FirewallProfile]**](FirewallProfile.md) | Specifies the firewall profiles. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.firewall_entry import FirewallEntry

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallEntry from a JSON string
firewall_entry_instance = FirewallEntry.from_json(json)
# print the JSON string representation of the object
print(FirewallEntry.to_json())

# convert the object into a dict
firewall_entry_dict = firewall_entry_instance.to_dict()
# create an instance of FirewallEntry from a dict
firewall_entry_from_dict = FirewallEntry.from_dict(firewall_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


