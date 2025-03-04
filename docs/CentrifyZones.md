# CentrifyZones

Specifies a list of centrify zones for a domain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**centrify_zones** | [**List[CentrifyZone]**](CentrifyZone.md) | Specifies a list of centrify zones for this domain. | [optional] 
**domain_name** | **str** | Specifies a domain name with these centrify zones. | [optional] 

## Example

```python
from cohesity_sdk.models.centrify_zones import CentrifyZones

# TODO update the JSON string below
json = "{}"
# create an instance of CentrifyZones from a JSON string
centrify_zones_instance = CentrifyZones.from_json(json)
# print the JSON string representation of the object
print(CentrifyZones.to_json())

# convert the object into a dict
centrify_zones_dict = centrify_zones_instance.to_dict()
# create an instance of CentrifyZones from a dict
centrify_zones_from_dict = CentrifyZones.from_dict(centrify_zones_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


