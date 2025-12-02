# GraphEdge

Determines information about an edge in the graph.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dest_node_id** | **str** | Specifies Unique ID of the destination node. | [optional] [readonly] 
**dest_node_type** | **str** | Specifies the type of destination node. | [optional] 
**name** | **str** | Specifies the display name to be specified for relation. | [optional] 
**relation_attributes** | [**List[KeyValuePair]**](KeyValuePair.md) | Specifies the list of node relation attributes provided in key/value pair. | [optional] 
**relation_type** | **str** | Specified type of the edge relation type with node. | [optional] 
**src_node_id** | **str** | Specifies Unique ID of the source node. | [optional] [readonly] 
**src_node_type** | **str** | Specifies the type of source node. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.graph_edge import GraphEdge

# TODO update the JSON string below
json = "{}"
# create an instance of GraphEdge from a JSON string
graph_edge_instance = GraphEdge.from_json(json)
# print the JSON string representation of the object
print(GraphEdge.to_json())

# convert the object into a dict
graph_edge_dict = graph_edge_instance.to_dict()
# create an instance of GraphEdge from a dict
graph_edge_from_dict = GraphEdge.from_dict(graph_edge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


