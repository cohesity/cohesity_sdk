# AdCentrifyTypeParams

Specifies the properties associated to a Centrify type user id mapping.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Specifies a description of the Centrify zone. | 
**distinguished_name** | **str** | Specifies the distinguished name of the Centrify zone. | 
**var_schema** | **str** | Specifies the schema of this Centrify zone. | 
**zone_domain** | **str** | Specifies the zone domain of the Centrify zone. | [optional] [readonly] 
**zone_name** | **str** | Specifies the zone name of the Centrify zone. | [optional] [readonly] 
**fallback_option** | [**FallbackUserIdMappingParams**](FallbackUserIdMappingParams.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.ad_centrify_type_params import AdCentrifyTypeParams

# TODO update the JSON string below
json = "{}"
# create an instance of AdCentrifyTypeParams from a JSON string
ad_centrify_type_params_instance = AdCentrifyTypeParams.from_json(json)
# print the JSON string representation of the object
print(AdCentrifyTypeParams.to_json())

# convert the object into a dict
ad_centrify_type_params_dict = ad_centrify_type_params_instance.to_dict()
# create an instance of AdCentrifyTypeParams from a dict
ad_centrify_type_params_from_dict = AdCentrifyTypeParams.from_dict(ad_centrify_type_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


