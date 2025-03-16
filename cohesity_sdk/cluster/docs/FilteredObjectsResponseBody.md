# FilteredObjectsResponseBody

Specifies the filter details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filtered_objects** | [**List[FilteredObject]**](FilteredObject.md) | Specifies the list of filtered Objects. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.filtered_objects_response_body import FilteredObjectsResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of FilteredObjectsResponseBody from a JSON string
filtered_objects_response_body_instance = FilteredObjectsResponseBody.from_json(json)
# print the JSON string representation of the object
print(FilteredObjectsResponseBody.to_json())

# convert the object into a dict
filtered_objects_response_body_dict = filtered_objects_response_body_instance.to_dict()
# create an instance of FilteredObjectsResponseBody from a dict
filtered_objects_response_body_from_dict = FilteredObjectsResponseBody.from_dict(filtered_objects_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


