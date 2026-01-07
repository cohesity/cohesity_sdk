# PaginationParams

Specifies the cursor based pagination parameters for Protection Source and its children. Pagination is supported at a given level within the Protection Source Hierarchy with the help of before or after cursors. A Cursor will always refer to a specific source within the source dataset but will be invalidated if the item is removed.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **int, none_type** | Specifies the entity id for the Node at any level within the Source entity hierarchy whose children are to be paginated. | 
**page_size** | **int, none_type** | Specifies the maximum number of entities to be returned within the page. | [optional] 
**pagination_cursor** | [**PaginationCursor**](PaginationCursor.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


