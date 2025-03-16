# ProtectedObjectsSearchResponseBody

Specifies the Protected Objects search result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**ProtectedObjectsSearchMetadata**](ProtectedObjectsSearchMetadata.md) | Specifies the metadata information about the Protection Groups, Protection Policy etc., for search result. | [optional] 
**num_results** | **int** | Specifies the total number of search results which matches the search criteria. | [optional] 
**objects** | [**List[ProtectedObject]**](ProtectedObject.md) | Specifies the list of Protected Objects. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.protected_objects_search_response_body import ProtectedObjectsSearchResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectedObjectsSearchResponseBody from a JSON string
protected_objects_search_response_body_instance = ProtectedObjectsSearchResponseBody.from_json(json)
# print the JSON string representation of the object
print(ProtectedObjectsSearchResponseBody.to_json())

# convert the object into a dict
protected_objects_search_response_body_dict = protected_objects_search_response_body_instance.to_dict()
# create an instance of ProtectedObjectsSearchResponseBody from a dict
protected_objects_search_response_body_from_dict = ProtectedObjectsSearchResponseBody.from_dict(protected_objects_search_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


