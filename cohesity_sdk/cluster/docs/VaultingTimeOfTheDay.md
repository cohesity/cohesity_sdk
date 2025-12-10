# VaultingTimeOfTheDay

Vaulting time of the day.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hour** | **int** | Specifies the hour of the day (0-23). | 
**minute** | **int** | Specifies the minute of the hour (0-59). | 

## Example

```python
from cohesity_sdk.cluster.models.vaulting_time_of_the_day import VaultingTimeOfTheDay

# TODO update the JSON string below
json = "{}"
# create an instance of VaultingTimeOfTheDay from a JSON string
vaulting_time_of_the_day_instance = VaultingTimeOfTheDay.from_json(json)
# print the JSON string representation of the object
print(VaultingTimeOfTheDay.to_json())

# convert the object into a dict
vaulting_time_of_the_day_dict = vaulting_time_of_the_day_instance.to_dict()
# create an instance of VaultingTimeOfTheDay from a dict
vaulting_time_of_the_day_from_dict = VaultingTimeOfTheDay.from_dict(vaulting_time_of_the_day_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


