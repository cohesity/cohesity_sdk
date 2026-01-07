# GetGraphNodeDetailsRequestParams

Specifies the request parameters to query graph node relations for a given node id.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_type** | **str** | Specifies the node type | 
**count** | **int** | Specifies the number of graph node relations to be fetched for the specified pagination cookie. | [optional] 
**include_attributes** | **bool, none_type** | If set to false the response will only return name, type and is_root fields filled in each node/relation. If set to true all the attributes for the nodes and its relations are also returned. Defaults to true. | [optional] 
**pagination_cookie** | **str, none_type** | Specifies a cookie which can be passed in by the user in order to retrieve the next page of results. | [optional] 
**query_relation** | **bool, none_type** | If set to false only the node info will be returned, else the relations matching the below relation filters will be returned. Defaults to false. | [optional] 
**relation_filter** | [**GraphNodeRelationFilterParams**](GraphNodeRelationFilterParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


