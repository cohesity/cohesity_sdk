# FallbackUserIdMappingParams

Specifies a fallback param for Unix and Windows users mapping.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixed_type_params** | [**AdFixedTypeParams**](AdFixedTypeParams.md) |  | [optional] 
**type** | **str** | Specifies the type of the mapping. | 

## Example

```python
from cohesity_sdk.models.fallback_user_id_mapping_params import FallbackUserIdMappingParams

# TODO update the JSON string below
json = "{}"
# create an instance of FallbackUserIdMappingParams from a JSON string
fallback_user_id_mapping_params_instance = FallbackUserIdMappingParams.from_json(json)
# print the JSON string representation of the object
print(FallbackUserIdMappingParams.to_json())

# convert the object into a dict
fallback_user_id_mapping_params_dict = fallback_user_id_mapping_params_instance.to_dict()
# create an instance of FallbackUserIdMappingParams from a dict
fallback_user_id_mapping_params_from_dict = FallbackUserIdMappingParams.from_dict(fallback_user_id_mapping_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


