# DiffGraphNodeRelation

Definition of graph node relation difference between two snapshots.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diff_graph_node** | [**DiffGraphNode**](DiffGraphNode.md) |  | [optional] 
**diff_relations** | [**List[DiffGraphNodeEdge]**](DiffGraphNodeEdge.md) | Specifies the all pair of edges/node relations which are added, deleted or modified | [optional] 
**src_node_id** | **str** | Specifies Unique ID of the source node. | [optional] [readonly] 
**unmodified_relations** | [**List[GraphEdge]**](GraphEdge.md) | Specifies the list of all the edges which are unmodified. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.diff_graph_node_relation import DiffGraphNodeRelation

# TODO update the JSON string below
json = "{}"
# create an instance of DiffGraphNodeRelation from a JSON string
diff_graph_node_relation_instance = DiffGraphNodeRelation.from_json(json)
# print the JSON string representation of the object
print(DiffGraphNodeRelation.to_json())

# convert the object into a dict
diff_graph_node_relation_dict = diff_graph_node_relation_instance.to_dict()
# create an instance of DiffGraphNodeRelation from a dict
diff_graph_node_relation_from_dict = DiffGraphNodeRelation.from_dict(diff_graph_node_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


