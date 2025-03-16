# McmObjectLastRunActivities

Last protection runs info of objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_last_runs** | [**List[McmObjectActivity]**](McmObjectActivity.md) | Specifies a list of last protection run activities of objects. | [optional] 
**stats** | [**List[McmObjectActivityStats]**](McmObjectActivityStats.md) | Specifies the stats of object activity. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_object_last_run_activities import McmObjectLastRunActivities

# TODO update the JSON string below
json = "{}"
# create an instance of McmObjectLastRunActivities from a JSON string
mcm_object_last_run_activities_instance = McmObjectLastRunActivities.from_json(json)
# print the JSON string representation of the object
print(McmObjectLastRunActivities.to_json())

# convert the object into a dict
mcm_object_last_run_activities_dict = mcm_object_last_run_activities_instance.to_dict()
# create an instance of McmObjectLastRunActivities from a dict
mcm_object_last_run_activities_from_dict = McmObjectLastRunActivities.from_dict(mcm_object_last_run_activities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


