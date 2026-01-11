# QueryGraphNodesDiffParams

Specify the query params to determine difference of graph nodes between two snapshots for a given session id.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Specifies the number of objects to be fetched for the specified pagination cookie. | [optional] 
**diff_types** | **[str], none_type** | Specifies an optional mask to filter only certain kinds of diffs. Supported diff types - Added/Modified/Deleted/Unmodified | [optional] 
**node_filter** | [**GraphNodeFilterParams**](GraphNodeFilterParams.md) |  | [optional] 
**pagination_cookie** | **str, none_type** | Specifies a cookie which can be passed in by the user in order to retrieve the next page of results. | [optional] 
**session_id** | **str, none_type** | Specifies the id of the session for which diff of nodes has to be fetched. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


