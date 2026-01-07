# GetGraphNodeRelationsDiffParams

Specify the query params to determine difference of node relation between two snapshots for a given node id.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diff_relation** | **bool, none_type** | If set to false only the diff of node info will be returned else the diff of relations matching the below edge filters will also be returned. Defaults to false. | [optional] 
**diff_types** | **[str], none_type** | Specifies an optional mask to filter only certain kinds of diffs. Supported diff types - Added/Modified/Deleted/Unmodified | [optional] 
**relation_filter** | [**GraphNodeRelationFilterParams**](GraphNodeRelationFilterParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


