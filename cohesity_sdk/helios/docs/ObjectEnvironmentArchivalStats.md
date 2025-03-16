# ObjectEnvironmentArchivalStats

Defines the stats of objects in archival runs for an environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | Specifies the environment. | [optional] 
**num_successful_objects** | **int** | Specifies the number of successful objects. | [optional] 
**num_unsuccessful_objects** | **int** | Specifies the number of unsuccessful objects. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.object_environment_archival_stats import ObjectEnvironmentArchivalStats

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectEnvironmentArchivalStats from a JSON string
object_environment_archival_stats_instance = ObjectEnvironmentArchivalStats.from_json(json)
# print the JSON string representation of the object
print(ObjectEnvironmentArchivalStats.to_json())

# convert the object into a dict
object_environment_archival_stats_dict = object_environment_archival_stats_instance.to_dict()
# create an instance of ObjectEnvironmentArchivalStats from a dict
object_environment_archival_stats_from_dict = ObjectEnvironmentArchivalStats.from_dict(object_environment_archival_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


