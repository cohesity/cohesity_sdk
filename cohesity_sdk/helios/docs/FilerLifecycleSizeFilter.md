# FilerLifecycleSizeFilter

Specifies the Lifecycle Size Filter information with minimum and maximum values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_bytes** | **int** | Specifies the maximum size in bytes. | [optional] 
**min_bytes** | **int** | Specifies the minimum size in bytes. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.filer_lifecycle_size_filter import FilerLifecycleSizeFilter

# TODO update the JSON string below
json = "{}"
# create an instance of FilerLifecycleSizeFilter from a JSON string
filer_lifecycle_size_filter_instance = FilerLifecycleSizeFilter.from_json(json)
# print the JSON string representation of the object
print(FilerLifecycleSizeFilter.to_json())

# convert the object into a dict
filer_lifecycle_size_filter_dict = filer_lifecycle_size_filter_instance.to_dict()
# create an instance of FilerLifecycleSizeFilter from a dict
filer_lifecycle_size_filter_from_dict = FilerLifecycleSizeFilter.from_dict(filer_lifecycle_size_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


