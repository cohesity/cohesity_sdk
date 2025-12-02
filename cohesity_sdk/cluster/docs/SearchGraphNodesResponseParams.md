# SearchGraphNodesResponseParams

Specifies list of graph nodes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph_nodes** | [**List[GraphNodeResult]**](GraphNodeResult.md) | Specifies list of graph nodes. | [optional] 
**pagination_cookie** | **str** | Specifies the pagination cookie with which subsequent parts of the response can be fetched. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.search_graph_nodes_response_params import SearchGraphNodesResponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of SearchGraphNodesResponseParams from a JSON string
search_graph_nodes_response_params_instance = SearchGraphNodesResponseParams.from_json(json)
# print the JSON string representation of the object
print(SearchGraphNodesResponseParams.to_json())

# convert the object into a dict
search_graph_nodes_response_params_dict = search_graph_nodes_response_params_instance.to_dict()
# create an instance of SearchGraphNodesResponseParams from a dict
search_graph_nodes_response_params_from_dict = SearchGraphNodesResponseParams.from_dict(search_graph_nodes_response_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


