# WormProperties

Specifies the WORM related properties for this archive.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_archive_worm_compliant** | **bool** | Specifies whether this archive run is WORM compliant | [optional] 
**worm_expiry_time_usecs** | **int** | Specifies the time at which the WORM protection expires. | [optional] 
**worm_non_compliance_reason** | **str** | Specifies reason of archive not being worm compliant. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.worm_properties import WormProperties

# TODO update the JSON string below
json = "{}"
# create an instance of WormProperties from a JSON string
worm_properties_instance = WormProperties.from_json(json)
# print the JSON string representation of the object
print(WormProperties.to_json())

# convert the object into a dict
worm_properties_dict = worm_properties_instance.to_dict()
# create an instance of WormProperties from a dict
worm_properties_from_dict = WormProperties.from_dict(worm_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


