# UpdateFirewallRequest

Specifies the parameters to configure firewall settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**FirewallEntry**](FirewallEntry.md) |  | 
**update_attachment** | **bool** | If true, updates the firewall attachments. | [default to False]
**update_ipset** | **bool** | If true, updates the firewall IP sets. | [default to False]
**update_profile** | **bool** | If true, updates the firewall profiles. | [default to False]

## Example

```python
from cohesity_sdk.cluster.models.update_firewall_request import UpdateFirewallRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFirewallRequest from a JSON string
update_firewall_request_instance = UpdateFirewallRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateFirewallRequest.to_json())

# convert the object into a dict
update_firewall_request_dict = update_firewall_request_instance.to_dict()
# create an instance of UpdateFirewallRequest from a dict
update_firewall_request_from_dict = UpdateFirewallRequest.from_dict(update_firewall_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


