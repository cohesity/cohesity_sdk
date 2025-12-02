# GraphNodeResult

Specifies the information about graph node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**Error**](Error.md) |  | [optional] 
**graph_node_info** | [**GraphNode**](GraphNode.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.graph_node_result import GraphNodeResult

# TODO update the JSON string below
json = "{}"
# create an instance of GraphNodeResult from a JSON string
graph_node_result_instance = GraphNodeResult.from_json(json)
# print the JSON string representation of the object
print(GraphNodeResult.to_json())

# convert the object into a dict
graph_node_result_dict = graph_node_result_instance.to_dict()
# create an instance of GraphNodeResult from a dict
graph_node_result_from_dict = GraphNodeResult.from_dict(graph_node_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


