# AdNisProviderTypeParams

Specifies the properties associated to a NisProvider type user id mapping.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fallback_option** | [**FallbackUserIdMappingParams**](FallbackUserIdMappingParams.md) | Specifies a fallback user id mapping param in case the primary config does not work. | 

## Example

```python
from cohesity_sdk.helios.models.ad_nis_provider_type_params import AdNisProviderTypeParams

# TODO update the JSON string below
json = "{}"
# create an instance of AdNisProviderTypeParams from a JSON string
ad_nis_provider_type_params_instance = AdNisProviderTypeParams.from_json(json)
# print the JSON string representation of the object
print(AdNisProviderTypeParams.to_json())

# convert the object into a dict
ad_nis_provider_type_params_dict = ad_nis_provider_type_params_instance.to_dict()
# create an instance of AdNisProviderTypeParams from a dict
ad_nis_provider_type_params_from_dict = AdNisProviderTypeParams.from_dict(ad_nis_provider_type_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


