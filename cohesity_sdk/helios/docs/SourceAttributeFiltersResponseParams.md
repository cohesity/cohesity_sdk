# SourceAttributeFiltersResponseParams

Protection Source attribute filters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_attribute_filters** | [**List[SourceAttributeFilter]**](SourceAttributeFilter.md) | Specifies the list of protection source filters. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.source_attribute_filters_response_params import SourceAttributeFiltersResponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of SourceAttributeFiltersResponseParams from a JSON string
source_attribute_filters_response_params_instance = SourceAttributeFiltersResponseParams.from_json(json)
# print the JSON string representation of the object
print(SourceAttributeFiltersResponseParams.to_json())

# convert the object into a dict
source_attribute_filters_response_params_dict = source_attribute_filters_response_params_instance.to_dict()
# create an instance of SourceAttributeFiltersResponseParams from a dict
source_attribute_filters_response_params_from_dict = SourceAttributeFiltersResponseParams.from_dict(source_attribute_filters_response_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


