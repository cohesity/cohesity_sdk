# InterfaceGroupParams

Parameters to update an interface group on the cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the interface group. | 
**network_params** | [**InterfaceGroupNetworkParams**](InterfaceGroupNetworkParams.md) |  | [optional] 
**node_interface_params** | [**List[NodeInterfaceParams]**](NodeInterfaceParams.md) | Node and interface parameters. | 
**type** | **str** | Type of the interface group. | 

## Example

```python
from cohesity_sdk.models.interface_group_params import InterfaceGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceGroupParams from a JSON string
interface_group_params_instance = InterfaceGroupParams.from_json(json)
# print the JSON string representation of the object
print(InterfaceGroupParams.to_json())

# convert the object into a dict
interface_group_params_dict = interface_group_params_instance.to_dict()
# create an instance of InterfaceGroupParams from a dict
interface_group_params_from_dict = InterfaceGroupParams.from_dict(interface_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


