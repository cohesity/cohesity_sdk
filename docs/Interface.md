# Interface

Network interface parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bond_members** | [**List[BondMember]**](BondMember.md) | Bond member details for bond interface. | [optional] 
**bonding_mode** | **str** | Bonding mode if this interface is a bond. | [optional] 
**default_route** | **bool** | Specifies whether or not this interface is the default route. | [optional] 
**gateway** | **str** | Gateway of the interface. | [optional] 
**group** | **str** | Group to which this interface belongs. | [optional] 
**id** | **int** | Id of the interface. | [optional] 
**ipv6_gateway** | **str** | The IPv6 gateway of the interface. | [optional] 
**ipv6_static** | **str** | Static IPv6 of the interface. | [optional] 
**ipv6_subnet** | **str** | The IPv6 subnet of the interface. | [optional] 
**is_connected** | **bool** | Specifies whether or not this interface is connected. | [optional] 
**is_up** | **bool** | Specifies whether or not the interface is up. | [optional] 
**mac_address** | **str** | MAC address of the interface. | [optional] 
**mtu** | **int** | MTU of the interface. | [optional] 
**name** | **str** | The name of the interface. | [optional] 
**role** | **str** | Role of the interface. | [optional] 
**services** | **List[str]** | Types of services this interface is used for. | [optional] 
**speed** | **str** | Speed of the interface. | [optional] 
**static_ip** | **str** | Static IP of the interface. | [optional] 
**stats** | [**InterfaceStats**](InterfaceStats.md) |  | [optional] 
**subnet** | **str** | Subnet of the interface. | [optional] 
**type** | **str** | The type of the interface. | [optional] 
**virtual_ip** | **str** | Virtual IP of the interface. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.interface import Interface

# TODO update the JSON string below
json = "{}"
# create an instance of Interface from a JSON string
interface_instance = Interface.from_json(json)
# print the JSON string representation of the object
print(Interface.to_json())

# convert the object into a dict
interface_dict = interface_instance.to_dict()
# create an instance of Interface from a dict
interface_from_dict = Interface.from_dict(interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


