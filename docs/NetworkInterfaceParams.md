# NetworkInterfaceParams

Network interfaces.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_network_interfaces** | [**List[NodeNetworkInterfaces]**](NodeNetworkInterfaces.md) | List of interfaces on each node. | [optional] 

## Example

```python
from cohesity_sdk.models.network_interface_params import NetworkInterfaceParams

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInterfaceParams from a JSON string
network_interface_params_instance = NetworkInterfaceParams.from_json(json)
# print the JSON string representation of the object
print(NetworkInterfaceParams.to_json())

# convert the object into a dict
network_interface_params_dict = network_interface_params_instance.to_dict()
# create an instance of NetworkInterfaceParams from a dict
network_interface_params_from_dict = NetworkInterfaceParams.from_dict(network_interface_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


