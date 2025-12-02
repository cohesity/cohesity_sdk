# NetworkInterface

Specifies the parameters of a network interface.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_bond_slave** | **str, none_type** | Current active slave. This is only valid in active-backup mode. | [optional] 
**bond_slave_names** | **[str], none_type** | Specifies the names of the bond slaves for this interface. | [optional] 
**bond_slave_slots** | **[str], none_type** | Specifies the slots of the bond slaves for this interface. | [optional] 
**bond_slaves_details** | [**[BondMember], none_type**](BondMember.md) | Bond member details for bond interface. | [optional] 
**bonding_mode** | **str, none_type** | Specifies the bonding mode of this interface. | [optional] 
**default_route** | **bool, none_type** | Specifies whether or not this interface is the default route. | [optional] 
**gateway** | **str, none_type** | Specifies the gateway of the network interface. | [optional] 
**gateway_v6** | **str, none_type** | Specifies the gatewayV6 of the network interface. | [optional] 
**group** | **str, none_type** | Specifies the group to which this interface belongs. | [optional] 
**is_connected** | **bool, none_type** | Specifies whether or not this interface is connected. | [optional] 
**is_up** | **bool, none_type** | Specifies whether or not the interface is up. | [optional] 
**mac_address** | **str, none_type** | Specifies the MAC address of this interface. | [optional] 
**mtu** | **int, none_type** | Specifies the MTU of the network interface. | [optional] 
**name** | **str, none_type** | Specifies the name of the network interface. | [optional] 
**role** | **str, none_type** | Specifies the interface role. | [optional] 
**services** | **[str], none_type** | Services which use this interface. | [optional] 
**speed** | **str, none_type** | Specifies the speed of this interface. | [optional] 
**static_ip** | **str, none_type** | Specifies the static IP of the network interface. | [optional] 
**static_ip_v6** | **str, none_type** | Specifies the static IPV6 of the network interface. | [optional] 
**stats** | [**InterfaceStats**](InterfaceStats.md) |  | [optional] 
**subnet** | **str, none_type** | Specifies the subnet of the network interface. | [optional] 
**subnet_v6** | **str, none_type** | Specifies the subnetV6 of the network interface. | [optional] 
**type** | **str, none_type** | Specifies the type of the network interface. | [optional] 
**virtual_ip** | **str, none_type** | Specifies the virtual IP of the network interface. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


