# CommonSearchIndexedObjectsResponseParams

Specifies the common search indexed objects response params.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Specifies the total number of indexed objects that match the filter and search criteria. Use this value to determine how many additional requests are required to get the full result. | [optional] 
**object_type** | **str** | Specifies the object type. | [optional] 
**pagination_cookie** | **str** | Specifies cookie for resuming search if pagination is being used. | [optional] 

## Example

```python
from cohesity_sdk.models.common_search_indexed_objects_response_params import CommonSearchIndexedObjectsResponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonSearchIndexedObjectsResponseParams from a JSON string
common_search_indexed_objects_response_params_instance = CommonSearchIndexedObjectsResponseParams.from_json(json)
# print the JSON string representation of the object
print(CommonSearchIndexedObjectsResponseParams.to_json())

# convert the object into a dict
common_search_indexed_objects_response_params_dict = common_search_indexed_objects_response_params_instance.to_dict()
# create an instance of CommonSearchIndexedObjectsResponseParams from a dict
common_search_indexed_objects_response_params_from_dict = CommonSearchIndexedObjectsResponseParams.from_dict(common_search_indexed_objects_response_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


