# DnsDelegationZone

Dns delegation zone of the vlan.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_zone_resolved_vips** | **List[str]** | Dns zone resolved VIPs. | [optional] 
**dns_zone_vips** | **List[str]** | VIPs part of dns zone. | [optional] 
**name** | **str** | Name of dns zone. | 

## Example

```python
from cohesity_sdk.models.dns_delegation_zone import DnsDelegationZone

# TODO update the JSON string below
json = "{}"
# create an instance of DnsDelegationZone from a JSON string
dns_delegation_zone_instance = DnsDelegationZone.from_json(json)
# print the JSON string representation of the object
print(DnsDelegationZone.to_json())

# convert the object into a dict
dns_delegation_zone_dict = dns_delegation_zone_instance.to_dict()
# create an instance of DnsDelegationZone from a dict
dns_delegation_zone_from_dict = DnsDelegationZone.from_dict(dns_delegation_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


