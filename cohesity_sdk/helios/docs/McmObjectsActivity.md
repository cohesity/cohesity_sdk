# McmObjectsActivity

Specifies the Objects activity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**List[McmObjectActivity]**](McmObjectActivity.md) | Specifies the activity list per object. | [optional] 
**is_refresh_task_active** | **bool** | Specifies if there is at least one active refresh task for refreshing activity data. The refresh tasks are triggered internally based on user actions such as protect now, pause backup, recovery, etc. The refresh tasks updates the activity details at a faster frequency. API consumers can choose to poll list activities API based on the status of this field to fetch the latest activity details. | [optional] 
**stats** | [**List[McmObjectActivityStats]**](McmObjectActivityStats.md) | Specifies the stats of object activity. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_objects_activity import McmObjectsActivity

# TODO update the JSON string below
json = "{}"
# create an instance of McmObjectsActivity from a JSON string
mcm_objects_activity_instance = McmObjectsActivity.from_json(json)
# print the JSON string representation of the object
print(McmObjectsActivity.to_json())

# convert the object into a dict
mcm_objects_activity_dict = mcm_objects_activity_instance.to_dict()
# create an instance of McmObjectsActivity from a dict
mcm_objects_activity_from_dict = McmObjectsActivity.from_dict(mcm_objects_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


