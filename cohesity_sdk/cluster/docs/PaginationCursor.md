# PaginationCursor

Specifies information needed to support pagination. The paginated Protection Source API response will contain the BeforeCursorEntityId, AfterCursorEntityId & the PageSize. It is the client's responsibility to keep a track of pagination params to invoke the next set of paged result.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after_cursor_entity_id** | **int, none_type** | Specifies the entity id starting from which the items are to be returned. | [optional] 
**before_cursor_entity_id** | **int, none_type** | Specifies the entity id upto which the items are to be returned. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


