# PaginationParams

Specifies the cursor based pagination parameters for Protection Source and its children. Pagination is supported at a given level within the Protection Source Hierarchy with the help of before or after cursors. A Cursor will always refer to a specific source within the source dataset but will be invalidated if the item is removed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **int** | Specifies the entity id for the Node at any level within the Source entity hierarchy whose children are to be paginated. | 
**page_size** | **int** | Specifies the maximum number of entities to be returned within the page. | [optional] 
**pagination_cursor** | [**PaginationCursor**](PaginationCursor.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.pagination_params import PaginationParams

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationParams from a JSON string
pagination_params_instance = PaginationParams.from_json(json)
# print the JSON string representation of the object
print(PaginationParams.to_json())

# convert the object into a dict
pagination_params_dict = pagination_params_instance.to_dict()
# create an instance of PaginationParams from a dict
pagination_params_from_dict = PaginationParams.from_dict(pagination_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


