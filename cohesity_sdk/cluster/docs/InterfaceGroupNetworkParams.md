# InterfaceGroupNetworkParams

Interface group network parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bond_interface_params** | [**BondInterfaceNetworkParams**](BondInterfaceNetworkParams.md) |  | [optional] 
**mtu** | **int** | MTU of the network interface group. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.interface_group_network_params import InterfaceGroupNetworkParams

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceGroupNetworkParams from a JSON string
interface_group_network_params_instance = InterfaceGroupNetworkParams.from_json(json)
# print the JSON string representation of the object
print(InterfaceGroupNetworkParams.to_json())

# convert the object into a dict
interface_group_network_params_dict = interface_group_network_params_instance.to_dict()
# create an instance of InterfaceGroupNetworkParams from a dict
interface_group_network_params_from_dict = InterfaceGroupNetworkParams.from_dict(interface_group_network_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


