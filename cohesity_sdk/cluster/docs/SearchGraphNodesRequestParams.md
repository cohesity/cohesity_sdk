# SearchGraphNodesRequestParams

Specifies the request parameters to query nodes in the graph for a given session id.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_filter** | **str** | Filter string for node attributes. This filter string is environment-specific and interpretable by respective environment only. | [optional] 
**name** | **str** | Filters the nodes based on provided current node display name. | [optional] 
**node_type** | **str** | Filter the nodes which matches with specified node type. | 
**root_only** | **bool** | If set to true only root nodes would be returned. A root node refers to nodes in the graph with no incoming edges. Defaults to false. | [optional] 
**aad_params** | [**AadGraphNodeFilterParams**](AadGraphNodeFilterParams.md) |  | [optional] 
**count** | **int** | Specifies the number of graph nodes to be fetched for the specified pagination cookie. | [optional] 
**include_attributes** | **bool** | If set to false the response will only return name, type and is_root fields filled in each node. If set to true all the attributes for the nodes are also returned. Defaults to true. | [optional] 
**pagination_cookie** | **str** | Specifies a cookie which can be passed in by the user in order to retrieve the next page of results. | [optional] 
**session_id** | **str** | Specifies the id of a Session. | 

## Example

```python
from cohesity_sdk.cluster.models.search_graph_nodes_request_params import SearchGraphNodesRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of SearchGraphNodesRequestParams from a JSON string
search_graph_nodes_request_params_instance = SearchGraphNodesRequestParams.from_json(json)
# print the JSON string representation of the object
print(SearchGraphNodesRequestParams.to_json())

# convert the object into a dict
search_graph_nodes_request_params_dict = search_graph_nodes_request_params_instance.to_dict()
# create an instance of SearchGraphNodesRequestParams from a dict
search_graph_nodes_request_params_from_dict = SearchGraphNodesRequestParams.from_dict(search_graph_nodes_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


