# DiffGraphNode

Definition of graph node difference between two snapshots.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_graph_node** | [**GraphNode**](GraphNode.md) |  | [optional] 
**current_graph_node** | [**GraphNode**](GraphNode.md) |  | [optional] 
**diff_type** | **str** | Specifies the diff type for the base node. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.diff_graph_node import DiffGraphNode

# TODO update the JSON string below
json = "{}"
# create an instance of DiffGraphNode from a JSON string
diff_graph_node_instance = DiffGraphNode.from_json(json)
# print the JSON string representation of the object
print(DiffGraphNode.to_json())

# convert the object into a dict
diff_graph_node_dict = diff_graph_node_instance.to_dict()
# create an instance of DiffGraphNode from a dict
diff_graph_node_from_dict = DiffGraphNode.from_dict(diff_graph_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


