# GetGraphNodeDetailsRequestParams

Specifies the request parameters to query graph node relations for a given node id.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Specifies the number of graph node relations to be fetched for the specified pagination cookie. | [optional] 
**include_attributes** | **bool** | If set to false the response will only return name, type and is_root fields filled in each node/relation. If set to true all the attributes for the nodes and its relations are also returned. Defaults to true. | [optional] 
**node_type** | **str** | Specifies the node type | 
**pagination_cookie** | **str** | Specifies a cookie which can be passed in by the user in order to retrieve the next page of results. | [optional] 
**query_relation** | **bool** | If set to false only the node info will be returned, else the relations matching the below relation filters will be returned. Defaults to false. | [optional] 
**relation_filter** | [**GraphNodeRelationFilterParams**](GraphNodeRelationFilterParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.get_graph_node_details_request_params import GetGraphNodeDetailsRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of GetGraphNodeDetailsRequestParams from a JSON string
get_graph_node_details_request_params_instance = GetGraphNodeDetailsRequestParams.from_json(json)
# print the JSON string representation of the object
print(GetGraphNodeDetailsRequestParams.to_json())

# convert the object into a dict
get_graph_node_details_request_params_dict = get_graph_node_details_request_params_instance.to_dict()
# create an instance of GetGraphNodeDetailsRequestParams from a dict
get_graph_node_details_request_params_from_dict = GetGraphNodeDetailsRequestParams.from_dict(get_graph_node_details_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


