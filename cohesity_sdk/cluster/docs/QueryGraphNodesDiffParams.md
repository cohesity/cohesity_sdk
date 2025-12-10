# QueryGraphNodesDiffParams

Specify the query params to determine difference of graph nodes between two snapshots for a given session id.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Specifies the number of objects to be fetched for the specified pagination cookie. | [optional] 
**diff_types** | **List[str]** | Specifies an optional mask to filter only certain kinds of diffs. Supported diff types - Added/Modified/Deleted/Unmodified | [optional] 
**node_filter** | [**GraphNodeFilterParams**](GraphNodeFilterParams.md) |  | [optional] 
**pagination_cookie** | **str** | Specifies a cookie which can be passed in by the user in order to retrieve the next page of results. | [optional] 
**session_id** | **str** | Specifies the id of the session for which diff of nodes has to be fetched. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.query_graph_nodes_diff_params import QueryGraphNodesDiffParams

# TODO update the JSON string below
json = "{}"
# create an instance of QueryGraphNodesDiffParams from a JSON string
query_graph_nodes_diff_params_instance = QueryGraphNodesDiffParams.from_json(json)
# print the JSON string representation of the object
print(QueryGraphNodesDiffParams.to_json())

# convert the object into a dict
query_graph_nodes_diff_params_dict = query_graph_nodes_diff_params_instance.to_dict()
# create an instance of QueryGraphNodesDiffParams from a dict
query_graph_nodes_diff_params_from_dict = QueryGraphNodesDiffParams.from_dict(query_graph_nodes_diff_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


