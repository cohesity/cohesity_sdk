# QueryGraphNodesDiffResult

Query result for Diff of nodes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diff_graph_nodes** | [**List[QueryGraphNodesDiffResultDiffGraphNodesInner]**](QueryGraphNodesDiffResultDiffGraphNodesInner.md) | Specifies the list of diff for all the nodes matching the filter | [optional] 
**pagination_cookie** | **str** | Specifies the pagination cookie with which subsequent parts of the response can be fetched. | [optional] 
**unmodified_graph_nodes** | **List[str]** | Specifies the list of all the graph node ids which are unmodified. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.query_graph_nodes_diff_result import QueryGraphNodesDiffResult

# TODO update the JSON string below
json = "{}"
# create an instance of QueryGraphNodesDiffResult from a JSON string
query_graph_nodes_diff_result_instance = QueryGraphNodesDiffResult.from_json(json)
# print the JSON string representation of the object
print(QueryGraphNodesDiffResult.to_json())

# convert the object into a dict
query_graph_nodes_diff_result_dict = query_graph_nodes_diff_result_instance.to_dict()
# create an instance of QueryGraphNodesDiffResult from a dict
query_graph_nodes_diff_result_from_dict = QueryGraphNodesDiffResult.from_dict(query_graph_nodes_diff_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


