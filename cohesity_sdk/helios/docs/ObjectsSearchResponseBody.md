# ObjectsSearchResponseBody

Specifies the Objects search result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Specifies the number of objects to be fetched for the specified pagination cookie. | [optional] 
**objects** | [**List[SearchObject]**](SearchObject.md) | Specifies the list of Objects. | [optional] 
**pagination_cookie** | **str** | Specifies the pagination cookie with which subsequent parts of the response can be fetched. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.objects_search_response_body import ObjectsSearchResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectsSearchResponseBody from a JSON string
objects_search_response_body_instance = ObjectsSearchResponseBody.from_json(json)
# print the JSON string representation of the object
print(ObjectsSearchResponseBody.to_json())

# convert the object into a dict
objects_search_response_body_dict = objects_search_response_body_instance.to_dict()
# create an instance of ObjectsSearchResponseBody from a dict
objects_search_response_body_from_dict = ObjectsSearchResponseBody.from_dict(objects_search_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


