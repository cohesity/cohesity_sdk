# GraphNodeFilterParams

Determines filter that can be applied to query node.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_type** | **str** | Filter the nodes which matches with specified node type. | 
**name** | **str, none_type** | Filters the nodes based on provided current node display name. | [optional] 
**root_only** | **bool, none_type** | If set to true only root nodes would be returned. A root node refers to nodes in the graph with no incoming edges. Defaults to false. | [optional] 
**aad_params** | [**AadGraphNodeFilterParams**](AadGraphNodeFilterParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


