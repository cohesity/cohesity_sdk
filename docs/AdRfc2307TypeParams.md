# AdRfc2307TypeParams

Specifies the properties associated to a Rfc2307 type user id mapping.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fallback_option** | [**FallbackUserIdMappingParams**](FallbackUserIdMappingParams.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.ad_rfc2307_type_params import AdRfc2307TypeParams

# TODO update the JSON string below
json = "{}"
# create an instance of AdRfc2307TypeParams from a JSON string
ad_rfc2307_type_params_instance = AdRfc2307TypeParams.from_json(json)
# print the JSON string representation of the object
print(AdRfc2307TypeParams.to_json())

# convert the object into a dict
ad_rfc2307_type_params_dict = ad_rfc2307_type_params_instance.to_dict()
# create an instance of AdRfc2307TypeParams from a dict
ad_rfc2307_type_params_from_dict = AdRfc2307TypeParams.from_dict(ad_rfc2307_type_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


