# FleetTags

Specifies the fleet tag parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Specifies key for the fleet tag. | 
**value** | **str** | Specifies value for the fleet tag. | 

## Example

```python
from cohesity_sdk.models.fleet_tags import FleetTags

# TODO update the JSON string below
json = "{}"
# create an instance of FleetTags from a JSON string
fleet_tags_instance = FleetTags.from_json(json)
# print the JSON string representation of the object
print(FleetTags.to_json())

# convert the object into a dict
fleet_tags_dict = fleet_tags_instance.to_dict()
# create an instance of FleetTags from a dict
fleet_tags_from_dict = FleetTags.from_dict(fleet_tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


