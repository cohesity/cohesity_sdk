# SearchGraphNodesRequestParams

Specifies the request parameters to query nodes in the graph for a given session id.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_type** | **str** | Filter the nodes which matches with specified node type. | 
**session_id** | **str** | Specifies the id of a Session. | 
**attribute_filter** | **str, none_type** | Filter string for node attributes. This filter string is environment-specific and interpretable by respective environment only. | [optional] 
**name** | **str, none_type** | Filters the nodes based on provided current node display name. | [optional] 
**root_only** | **bool, none_type** | If set to true only root nodes would be returned. A root node refers to nodes in the graph with no incoming edges. Defaults to false. | [optional] 
**aad_params** | [**AadGraphNodeFilterParams**](AadGraphNodeFilterParams.md) |  | [optional] 
**count** | **int** | Specifies the number of graph nodes to be fetched for the specified pagination cookie. | [optional] 
**include_attributes** | **bool, none_type** | If set to false the response will only return name, type and is_root fields filled in each node. If set to true all the attributes for the nodes are also returned. Defaults to true. | [optional] 
**pagination_cookie** | **str, none_type** | Specifies a cookie which can be passed in by the user in order to retrieve the next page of results. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


