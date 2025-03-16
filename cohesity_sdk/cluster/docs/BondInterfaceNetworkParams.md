# BondInterfaceNetworkParams

Bond interface network parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bonding_mode** | **str** | Bonding mode of the interface. | [optional] 
**lacp_rate** | **str** | Rate option to use for link partner to transmit LACPDU packets in 802.3ad mode. | [optional] 
**xmit_hash_policy** | **str** | Transmit hash policy to use for selection in 802.3ad mode. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.bond_interface_network_params import BondInterfaceNetworkParams

# TODO update the JSON string below
json = "{}"
# create an instance of BondInterfaceNetworkParams from a JSON string
bond_interface_network_params_instance = BondInterfaceNetworkParams.from_json(json)
# print the JSON string representation of the object
print(BondInterfaceNetworkParams.to_json())

# convert the object into a dict
bond_interface_network_params_dict = bond_interface_network_params_instance.to_dict()
# create an instance of BondInterfaceNetworkParams from a dict
bond_interface_network_params_from_dict = BondInterfaceNetworkParams.from_dict(bond_interface_network_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


