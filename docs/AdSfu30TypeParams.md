# AdSfu30TypeParams

Specifies the properties associated to a Sfu30 type user id mapping.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fallback_option** | [**FallbackUserIdMappingParams**](FallbackUserIdMappingParams.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.ad_sfu30_type_params import AdSfu30TypeParams

# TODO update the JSON string below
json = "{}"
# create an instance of AdSfu30TypeParams from a JSON string
ad_sfu30_type_params_instance = AdSfu30TypeParams.from_json(json)
# print the JSON string representation of the object
print(AdSfu30TypeParams.to_json())

# convert the object into a dict
ad_sfu30_type_params_dict = ad_sfu30_type_params_instance.to_dict()
# create an instance of AdSfu30TypeParams from a dict
ad_sfu30_type_params_from_dict = AdSfu30TypeParams.from_dict(ad_sfu30_type_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


