# SourceAttributeFilter

Specifies a pair of source filter attribute and its possible values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_values** | **List[str]** | Specifies the list of attribute values for above filter. | [optional] 
**filter_attribute** | **str** | Specifies the filter attribute for the source. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.source_attribute_filter import SourceAttributeFilter

# TODO update the JSON string below
json = "{}"
# create an instance of SourceAttributeFilter from a JSON string
source_attribute_filter_instance = SourceAttributeFilter.from_json(json)
# print the JSON string representation of the object
print(SourceAttributeFilter.to_json())

# convert the object into a dict
source_attribute_filter_dict = source_attribute_filter_instance.to_dict()
# create an instance of SourceAttributeFilter from a dict
source_attribute_filter_from_dict = SourceAttributeFilter.from_dict(source_attribute_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


