# InterfaceNetworkParams

Interface network parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bond_interface_params** | [**BondInterfaceNetworkParams**](BondInterfaceNetworkParams.md) |  | [optional] 
**mtu** | **int** | MTU of the network interface. | [optional] 

## Example

```python
from cohesity_sdk.models.interface_network_params import InterfaceNetworkParams

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceNetworkParams from a JSON string
interface_network_params_instance = InterfaceNetworkParams.from_json(json)
# print the JSON string representation of the object
print(InterfaceNetworkParams.to_json())

# convert the object into a dict
interface_network_params_dict = interface_network_params_instance.to_dict()
# create an instance of InterfaceNetworkParams from a dict
interface_network_params_from_dict = InterfaceNetworkParams.from_dict(interface_network_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


