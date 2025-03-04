# FreeNodes

Specifies the free nodes information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**List[FreeNodeInformation]**](FreeNodeInformation.md) | Specifies the list of free nodes. | [optional] 

## Example

```python
from cohesity_sdk.models.free_nodes import FreeNodes

# TODO update the JSON string below
json = "{}"
# create an instance of FreeNodes from a JSON string
free_nodes_instance = FreeNodes.from_json(json)
# print the JSON string representation of the object
print(FreeNodes.to_json())

# convert the object into a dict
free_nodes_dict = free_nodes_instance.to_dict()
# create an instance of FreeNodes from a dict
free_nodes_from_dict = FreeNodes.from_dict(free_nodes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


