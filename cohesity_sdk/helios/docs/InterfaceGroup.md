# InterfaceGroup

Interface group paramters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the interface group. | 
**network_params** | [**InterfaceGroupNetworkParams**](InterfaceGroupNetworkParams.md) |  | [optional] 
**node_interface_params** | [**List[NodeInterfaceParams]**](NodeInterfaceParams.md) | Node and interface parameters. | 
**type** | **str** | Type of the interface group. | 
**id** | **int** | Id of the interface group. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.interface_group import InterfaceGroup

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceGroup from a JSON string
interface_group_instance = InterfaceGroup.from_json(json)
# print the JSON string representation of the object
print(InterfaceGroup.to_json())

# convert the object into a dict
interface_group_dict = interface_group_instance.to_dict()
# create an instance of InterfaceGroup from a dict
interface_group_from_dict = InterfaceGroup.from_dict(interface_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


