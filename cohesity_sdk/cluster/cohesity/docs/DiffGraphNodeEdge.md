# DiffGraphNodeEdge

Represents the pair of edges and destination node which are either modified, added, deleted or unmodified compared to base snapshot.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_relation** | [**GraphEdge**](GraphEdge.md) |  | [optional] 
**current_relation** | [**GraphEdge**](GraphEdge.md) |  | [optional] 
**diff_type** | **str, none_type** | Specifies the diff type for the base node. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


