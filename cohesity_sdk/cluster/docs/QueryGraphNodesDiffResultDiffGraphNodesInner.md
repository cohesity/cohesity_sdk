# QueryGraphNodesDiffResultDiffGraphNodesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**Error**](Error.md) | Error is set if there was an error in looking up information for the node either in current or base snapshot. In case of error graphNodeInfo will only have the node id. | [optional] 
**graph_node_info** | [**DiffGraphNode**](DiffGraphNode.md) | Specifies the list of diff for all the nodes added/ deleted/modified. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.query_graph_nodes_diff_result_diff_graph_nodes_inner import QueryGraphNodesDiffResultDiffGraphNodesInner

# TODO update the JSON string below
json = "{}"
# create an instance of QueryGraphNodesDiffResultDiffGraphNodesInner from a JSON string
query_graph_nodes_diff_result_diff_graph_nodes_inner_instance = QueryGraphNodesDiffResultDiffGraphNodesInner.from_json(json)
# print the JSON string representation of the object
print(QueryGraphNodesDiffResultDiffGraphNodesInner.to_json())

# convert the object into a dict
query_graph_nodes_diff_result_diff_graph_nodes_inner_dict = query_graph_nodes_diff_result_diff_graph_nodes_inner_instance.to_dict()
# create an instance of QueryGraphNodesDiffResultDiffGraphNodesInner from a dict
query_graph_nodes_diff_result_diff_graph_nodes_inner_from_dict = QueryGraphNodesDiffResultDiffGraphNodesInner.from_dict(query_graph_nodes_diff_result_diff_graph_nodes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


