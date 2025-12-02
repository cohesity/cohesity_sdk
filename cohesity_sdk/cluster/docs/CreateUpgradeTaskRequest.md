# CreateUpgradeTaskRequest

Specifies the params to create a schedule based agent upgrade task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_ids** | **List[int]** | Specifies agent IDs to be upgraded in the task. | [optional] 
**description** | **str** | Specifies the description of the task. | [optional] 
**name** | **str** | Specifies the name of the task. | [optional] 
**retry_task_id** | **int** | Specifies the task that needs to be retried. | [optional] 
**schedule_end_time_usecs** | **int** | Specifies the time before which the upgrade task should start execution as a Unix epoch Timestamp (in microseconds). If this is not specified the task will start anytime after scheduleTimeUsecs. | [optional] 
**schedule_time_usecs** | **int** | Specifies the start time of the task specified by the user as a Unix epoch Timestamp (in microseconds). If no schedule is specified, the agents will be upgraded immediately. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.create_upgrade_task_request import CreateUpgradeTaskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUpgradeTaskRequest from a JSON string
create_upgrade_task_request_instance = CreateUpgradeTaskRequest.from_json(json)
# print the JSON string representation of the object
print(CreateUpgradeTaskRequest.to_json())

# convert the object into a dict
create_upgrade_task_request_dict = create_upgrade_task_request_instance.to_dict()
# create an instance of CreateUpgradeTaskRequest from a dict
create_upgrade_task_request_from_dict = CreateUpgradeTaskRequest.from_dict(create_upgrade_task_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


