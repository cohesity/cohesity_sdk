# GraphNode

Determines information about a node in the graph.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aad_params** | [**AadNodeInfo**](AadNodeInfo.md) |  | [optional] 
**is_root_node** | **bool** | Boolean to indicate if this is a root node or not. | [optional] 
**name** | **str** | Specifies the display name of the node. | [optional] 
**node_id** | **str** | Specifies the unique id of the node. | 
**node_type** | **str** | Specifies the type of aad node. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.graph_node import GraphNode

# TODO update the JSON string below
json = "{}"
# create an instance of GraphNode from a JSON string
graph_node_instance = GraphNode.from_json(json)
# print the JSON string representation of the object
print(GraphNode.to_json())

# convert the object into a dict
graph_node_dict = graph_node_instance.to_dict()
# create an instance of GraphNode from a dict
graph_node_from_dict = GraphNode.from_dict(graph_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


