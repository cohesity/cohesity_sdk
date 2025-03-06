# StandbyObject

Specifies the standby related information for a given VM object. This field will only be populated when standby is configured on the protection group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **int** | Specifies the entity id of the corresponding backup object for which this standby is configured. | [optional] 
**protection_group_id** | **str** | Specifies the protection group id to which this standby object belongs. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.standby_object import StandbyObject

# TODO update the JSON string below
json = "{}"
# create an instance of StandbyObject from a JSON string
standby_object_instance = StandbyObject.from_json(json)
# print the JSON string representation of the object
print(StandbyObject.to_json())

# convert the object into a dict
standby_object_dict = standby_object_instance.to_dict()
# create an instance of StandbyObject from a dict
standby_object_from_dict = StandbyObject.from_dict(standby_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


