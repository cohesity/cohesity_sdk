# DiffGraphNodeEdge

Represents the pair of edges and destination node which are either modified, added, deleted or unmodified compared to base snapshot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_relation** | [**GraphEdge**](GraphEdge.md) |  | [optional] 
**current_relation** | [**GraphEdge**](GraphEdge.md) |  | [optional] 
**diff_type** | **str** | Specifies the diff type for the base node. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.diff_graph_node_edge import DiffGraphNodeEdge

# TODO update the JSON string below
json = "{}"
# create an instance of DiffGraphNodeEdge from a JSON string
diff_graph_node_edge_instance = DiffGraphNodeEdge.from_json(json)
# print the JSON string representation of the object
print(DiffGraphNodeEdge.to_json())

# convert the object into a dict
diff_graph_node_edge_dict = diff_graph_node_edge_instance.to_dict()
# create an instance of DiffGraphNodeEdge from a dict
diff_graph_node_edge_from_dict = DiffGraphNodeEdge.from_dict(diff_graph_node_edge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


