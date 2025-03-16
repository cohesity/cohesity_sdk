# McmObjectActivityStats

Specifies the Object activity stats.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_count** | **int** | Specifies the count of activities. | [optional] 
**activity_type** | **str** | Type of the activity | [optional] 
**message_code** | **str** | Specifies a short message describing the type of error which occurred. | [optional] 
**object_environment** | **str** | Environment type of object. | [optional] 
**protection_environment** | **str** | Environment type of the protection. | [optional] 
**status** | **str** | Status of the activity | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_object_activity_stats import McmObjectActivityStats

# TODO update the JSON string below
json = "{}"
# create an instance of McmObjectActivityStats from a JSON string
mcm_object_activity_stats_instance = McmObjectActivityStats.from_json(json)
# print the JSON string representation of the object
print(McmObjectActivityStats.to_json())

# convert the object into a dict
mcm_object_activity_stats_dict = mcm_object_activity_stats_instance.to_dict()
# create an instance of McmObjectActivityStats from a dict
mcm_object_activity_stats_from_dict = McmObjectActivityStats.from_dict(mcm_object_activity_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


