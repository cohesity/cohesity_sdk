# ObjectStatsInfo

Specifies the Stats of an object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | [**ObjectStringIdentifier**](ObjectStringIdentifier.md) |  | [optional] 
**environment** | **str** | Specifies the environment of the object. | [optional] 
**id** | **int** | Specifies object id. | [optional] 
**name** | **str** | Specifies the name of the object. | [optional] 
**source_id** | **int** | Specifies registered source id to which object belongs. | [optional] 
**source_name** | **str** | Specifies registered source name to which object belongs. | [optional] 
**backup_generic_stats** | [**BackupGenericStats**](BackupGenericStats.md) |  | [optional] 
**nas_stats** | [**BackupNasStats**](BackupNasStats.md) |  | [optional] 
**failed_attempts** | [**List[StatsTaskInfo]**](StatsTaskInfo.md) | Specifies stats for failed attempts of this object. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.object_stats_info import ObjectStatsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectStatsInfo from a JSON string
object_stats_info_instance = ObjectStatsInfo.from_json(json)
# print the JSON string representation of the object
print(ObjectStatsInfo.to_json())

# convert the object into a dict
object_stats_info_dict = object_stats_info_instance.to_dict()
# create an instance of ObjectStatsInfo from a dict
object_stats_info_from_dict = ObjectStatsInfo.from_dict(object_stats_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


