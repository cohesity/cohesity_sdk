# PaginationCursor

Specifies information needed to support pagination. The paginated Protection Source API response will contain the BeforeCursorEntityId, AfterCursorEntityId & the PageSize. It is the client's responsibility to keep a track of pagination params to invoke the next set of paged result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after_cursor_entity_id** | **int** | Specifies the entity id starting from which the items are to be returned. | [optional] 
**before_cursor_entity_id** | **int** | Specifies the entity id upto which the items are to be returned. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.pagination_cursor import PaginationCursor

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationCursor from a JSON string
pagination_cursor_instance = PaginationCursor.from_json(json)
# print the JSON string representation of the object
print(PaginationCursor.to_json())

# convert the object into a dict
pagination_cursor_dict = pagination_cursor_instance.to_dict()
# create an instance of PaginationCursor from a dict
pagination_cursor_from_dict = PaginationCursor.from_dict(pagination_cursor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


