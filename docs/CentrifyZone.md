# CentrifyZone

Specifies a centrify zone.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Specifies a description of the Centrify zone. | 
**distinguished_name** | **str** | Specifies the distinguished name of the Centrify zone. | 
**var_schema** | **str** | Specifies the schema of this Centrify zone. | 
**zone_domain** | **str** | Specifies the zone domain of the Centrify zone. | [optional] [readonly] 
**zone_name** | **str** | Specifies the zone name of the Centrify zone. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.centrify_zone import CentrifyZone

# TODO update the JSON string below
json = "{}"
# create an instance of CentrifyZone from a JSON string
centrify_zone_instance = CentrifyZone.from_json(json)
# print the JSON string representation of the object
print(CentrifyZone.to_json())

# convert the object into a dict
centrify_zone_dict = centrify_zone_instance.to_dict()
# create an instance of CentrifyZone from a dict
centrify_zone_from_dict = CentrifyZone.from_dict(centrify_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


