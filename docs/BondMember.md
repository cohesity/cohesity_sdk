# BondMember

Bond member details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_secondary** | **bool** | Specifies whether or not this is a active secondary. This is only valid in ActiveBackup bonding mode. | [optional] 
**link_state** | **str** | Bond secondary link state. | [optional] 
**mac_address** | **str** | MAC address of the bond secondary. | [optional] 
**name** | **str** | Name of the bond secondary. | [optional] 
**slot** | **str** | Slot information of the bond secondary. | [optional] 
**speed** | **str** | Speed of the bond secondary. | [optional] 
**stats** | [**InterfaceStats**](InterfaceStats.md) |  | [optional] 
**uplink_switch** | [**UplinkSwitch**](UplinkSwitch.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.bond_member import BondMember

# TODO update the JSON string below
json = "{}"
# create an instance of BondMember from a JSON string
bond_member_instance = BondMember.from_json(json)
# print the JSON string representation of the object
print(BondMember.to_json())

# convert the object into a dict
bond_member_dict = bond_member_instance.to_dict()
# create an instance of BondMember from a dict
bond_member_from_dict = BondMember.from_dict(bond_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


