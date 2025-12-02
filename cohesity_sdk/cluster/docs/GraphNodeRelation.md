# GraphNodeRelation

Defintion of node relation spec.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph_node_info** | [**GraphNode**](GraphNode.md) |  | [optional] 
**relations** | [**List[GraphEdge]**](GraphEdge.md) | Specifies the list of related edges/neighbours/relations of the source graph node. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.graph_node_relation import GraphNodeRelation

# TODO update the JSON string below
json = "{}"
# create an instance of GraphNodeRelation from a JSON string
graph_node_relation_instance = GraphNodeRelation.from_json(json)
# print the JSON string representation of the object
print(GraphNodeRelation.to_json())

# convert the object into a dict
graph_node_relation_dict = graph_node_relation_instance.to_dict()
# create an instance of GraphNodeRelation from a dict
graph_node_relation_from_dict = GraphNodeRelation.from_dict(graph_node_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


