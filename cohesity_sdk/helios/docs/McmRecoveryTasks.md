# McmRecoveryTasks

Specifies the Recovery activities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recoveries** | [**List[McmRecoveryTask]**](McmRecoveryTask.md) | Specifies the recovery list. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_recovery_tasks import McmRecoveryTasks

# TODO update the JSON string below
json = "{}"
# create an instance of McmRecoveryTasks from a JSON string
mcm_recovery_tasks_instance = McmRecoveryTasks.from_json(json)
# print the JSON string representation of the object
print(McmRecoveryTasks.to_json())

# convert the object into a dict
mcm_recovery_tasks_dict = mcm_recovery_tasks_instance.to_dict()
# create an instance of McmRecoveryTasks from a dict
mcm_recovery_tasks_from_dict = McmRecoveryTasks.from_dict(mcm_recovery_tasks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


