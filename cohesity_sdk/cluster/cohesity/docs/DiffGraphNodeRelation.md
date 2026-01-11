# DiffGraphNodeRelation

Definition of graph node relation difference between two snapshots.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diff_graph_node** | [**DiffGraphNode**](DiffGraphNode.md) |  | [optional] 
**diff_relations** | [**[DiffGraphNodeEdge], none_type**](DiffGraphNodeEdge.md) | Specifies the all pair of edges/node relations which are added, deleted or modified | [optional] 
**src_node_id** | **str** | Specifies Unique ID of the source node. | [optional] [readonly] 
**unmodified_relations** | [**[GraphEdge], none_type**](GraphEdge.md) | Specifies the list of all the edges which are unmodified. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


