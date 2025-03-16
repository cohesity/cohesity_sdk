# FilteredObject

Specifies the filter details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies object id. | [optional] 
**source_id** | **int** | Specifies the source id to which this object belongs to. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.filtered_object import FilteredObject

# TODO update the JSON string below
json = "{}"
# create an instance of FilteredObject from a JSON string
filtered_object_instance = FilteredObject.from_json(json)
# print the JSON string representation of the object
print(FilteredObject.to_json())

# convert the object into a dict
filtered_object_dict = filtered_object_instance.to_dict()
# create an instance of FilteredObject from a dict
filtered_object_from_dict = FilteredObject.from_dict(filtered_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


