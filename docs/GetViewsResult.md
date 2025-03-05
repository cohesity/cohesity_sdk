# GetViewsResult

Specifies the list of Views returned that matched the specified filter criteria.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of views returned. This will only be returned if ViewCountOnly is set in arguments. | [optional] 
**last_result** | **bool** | If false, more Views are available to return. If the number of Views to return exceeds the number of Views specified in maxCount (default of 1000) of the original GET /public/views request, the first set of Views are returned and this field returns false. To get the next set of Views, in the next GET /public/views request send the last id from the previous viewList. | [optional] 
**views** | [**List[View]**](View.md) | Array of Views. Specifies the list of Views returned in this response. The list is sorted by decreasing View ids. | [optional] 

## Example

```python
from cohesity_sdk.models.get_views_result import GetViewsResult

# TODO update the JSON string below
json = "{}"
# create an instance of GetViewsResult from a JSON string
get_views_result_instance = GetViewsResult.from_json(json)
# print the JSON string representation of the object
print(GetViewsResult.to_json())

# convert the object into a dict
get_views_result_dict = get_views_result_instance.to_dict()
# create an instance of GetViewsResult from a dict
get_views_result_from_dict = GetViewsResult.from_dict(get_views_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


