# NodeInterfaceParams

Node and interface parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface_name** | **str** | Name of the interface. | [optional] 
**node_id** | **int** | Node id. | 

## Example

```python
from cohesity_sdk.models.node_interface_params import NodeInterfaceParams

# TODO update the JSON string below
json = "{}"
# create an instance of NodeInterfaceParams from a JSON string
node_interface_params_instance = NodeInterfaceParams.from_json(json)
# print the JSON string representation of the object
print(NodeInterfaceParams.to_json())

# convert the object into a dict
node_interface_params_dict = node_interface_params_instance.to_dict()
# create an instance of NodeInterfaceParams from a dict
node_interface_params_from_dict = NodeInterfaceParams.from_dict(node_interface_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


