# ObjectArchivalRunStats

Defines the stats of objects in archival runs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stats** | [**List[ObjectEnvironmentArchivalStats]**](ObjectEnvironmentArchivalStats.md) | Specifies stats for all the environments available. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.object_archival_run_stats import ObjectArchivalRunStats

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectArchivalRunStats from a JSON string
object_archival_run_stats_instance = ObjectArchivalRunStats.from_json(json)
# print the JSON string representation of the object
print(ObjectArchivalRunStats.to_json())

# convert the object into a dict
object_archival_run_stats_dict = object_archival_run_stats_instance.to_dict()
# create an instance of ObjectArchivalRunStats from a dict
object_archival_run_stats_from_dict = ObjectArchivalRunStats.from_dict(object_archival_run_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


