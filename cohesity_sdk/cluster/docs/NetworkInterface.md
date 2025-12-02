# NetworkInterface

Specifies the parameters of a network interface.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_bond_slave** | **str** | Current active slave. This is only valid in active-backup mode. | [optional] 
**bond_slave_names** | **List[str]** | Specifies the names of the bond slaves for this interface. | [optional] 
**bond_slave_slots** | **List[str]** | Specifies the slots of the bond slaves for this interface. | [optional] 
**bond_slaves_details** | [**List[BondMember]**](BondMember.md) | Bond member details for bond interface. | [optional] 
**bonding_mode** | **str** | Specifies the bonding mode of this interface. | [optional] 
**default_route** | **bool** | Specifies whether or not this interface is the default route. | [optional] 
**gateway** | **str** | Specifies the gateway of the network interface. | [optional] 
**gateway_v6** | **str** | Specifies the gatewayV6 of the network interface. | [optional] 
**group** | **str** | Specifies the group to which this interface belongs. | [optional] 
**is_connected** | **bool** | Specifies whether or not this interface is connected. | [optional] 
**is_up** | **bool** | Specifies whether or not the interface is up. | [optional] 
**mac_address** | **str** | Specifies the MAC address of this interface. | [optional] 
**mtu** | **int** | Specifies the MTU of the network interface. | [optional] 
**name** | **str** | Specifies the name of the network interface. | [optional] 
**role** | **str** | Specifies the interface role. | [optional] 
**services** | **List[str]** | Services which use this interface. | [optional] 
**speed** | **str** | Specifies the speed of this interface. | [optional] 
**static_ip** | **str** | Specifies the static IP of the network interface. | [optional] 
**static_ip_v6** | **str** | Specifies the static IPV6 of the network interface. | [optional] 
**stats** | [**InterfaceStats**](InterfaceStats.md) |  | [optional] 
**subnet** | **str** | Specifies the subnet of the network interface. | [optional] 
**subnet_v6** | **str** | Specifies the subnetV6 of the network interface. | [optional] 
**type** | **str** | Specifies the type of the network interface. | [optional] 
**virtual_ip** | **str** | Specifies the virtual IP of the network interface. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.network_interface import NetworkInterface

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInterface from a JSON string
network_interface_instance = NetworkInterface.from_json(json)
# print the JSON string representation of the object
print(NetworkInterface.to_json())

# convert the object into a dict
network_interface_dict = network_interface_instance.to_dict()
# create an instance of NetworkInterface from a dict
network_interface_from_dict = NetworkInterface.from_dict(network_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


