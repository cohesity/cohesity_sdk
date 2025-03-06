# RecoveryOracleTaskInfo

Specifies the info about a recovery task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time_usecs** | **int** | Specifies the end time in Unix timestamp epoch in microseconds. | [optional] [readonly] 
**progress_task_id** | **str** | Specifies the progress monitor id. | [optional] [readonly] 
**start_time_usecs** | **int** | Specifies the start time in Unix timestamp epoch in microseconds. | [optional] [readonly] 
**status** | **str** | Specifies the status of the recovery. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.recovery_oracle_task_info import RecoveryOracleTaskInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RecoveryOracleTaskInfo from a JSON string
recovery_oracle_task_info_instance = RecoveryOracleTaskInfo.from_json(json)
# print the JSON string representation of the object
print(RecoveryOracleTaskInfo.to_json())

# convert the object into a dict
recovery_oracle_task_info_dict = recovery_oracle_task_info_instance.to_dict()
# create an instance of RecoveryOracleTaskInfo from a dict
recovery_oracle_task_info_from_dict = RecoveryOracleTaskInfo.from_dict(recovery_oracle_task_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


