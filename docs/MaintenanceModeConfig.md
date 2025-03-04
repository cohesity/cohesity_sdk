# MaintenanceModeConfig

Specifies the entity metadata for maintenance mode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_time_intervals** | [**List[TimeRangeUsecs]**](TimeRangeUsecs.md) | Specifies the absolute intervals where the maintenance schedule is valid, i.e. maintenance_shedule is considered only for these time ranges. (For example, if there is one time range with [now_usecs, now_usecs + 10 days], the action will be done during the maintenance_schedule for the next 10 days.)The start time must be specified. The end time can be -1 which would denote an indefinite maintenance mode. | [optional] 
**maintenance_schedule** | [**Schedule**](Schedule.md) |  | [optional] 
**user_message** | **str** | User provided message associated with this maintenance mode. | [optional] 
**workflow_intervention_spec_list** | [**List[WorkflowInterventionSpec]**](WorkflowInterventionSpec.md) | Specifies the type of intervention for different workflows when the source goes into maintenance mode. | [optional] 

## Example

```python
from cohesity_sdk.models.maintenance_mode_config import MaintenanceModeConfig

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceModeConfig from a JSON string
maintenance_mode_config_instance = MaintenanceModeConfig.from_json(json)
# print the JSON string representation of the object
print(MaintenanceModeConfig.to_json())

# convert the object into a dict
maintenance_mode_config_dict = maintenance_mode_config_instance.to_dict()
# create an instance of MaintenanceModeConfig from a dict
maintenance_mode_config_from_dict = MaintenanceModeConfig.from_dict(maintenance_mode_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


