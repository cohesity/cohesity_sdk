# CommonDataTieringTaskResponse

Specifies the data tiering task details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_policy** | [**ProtectionGroupAlertingPolicy**](ProtectionGroupAlertingPolicy.md) |  | [optional] 
**description** | **str** | Specifies a description of the data tiering task. | [optional] 
**id** | **str** | Specifies the id of the data tiering task. | [optional] 
**is_active** | **bool** | Whether the data tiering task is active or not. | [optional] [default to True]
**is_deleted** | **bool** | Tracks whether the backup job has actually been deleted. | [optional] [default to True]
**is_paused** | **bool** | Whether the data tiering task is paused. New runs are not scheduled for the paused tasks. Active run of the task (if any) is not impacted. | [optional] [default to True]
**last_run** | [**DataTieringTaskRun**](DataTieringTaskRun.md) |  | [optional] 
**name** | **str** | Specifies the name of the data tiering task. | 
**schedule** | [**DataTieringSchedule**](DataTieringSchedule.md) |  | [optional] 
**source** | [**DataTieringSource**](DataTieringSource.md) |  | [optional] 
**target** | [**DataTieringTarget**](DataTieringTarget.md) |  | [optional] 
**type** | **str** | Type of data tiering task. &#39;Downtier&#39; indicates downtiering task. &#39;Uptier&#39; indicates uptiering task. | 

## Example

```python
from cohesity_sdk.models.common_data_tiering_task_response import CommonDataTieringTaskResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommonDataTieringTaskResponse from a JSON string
common_data_tiering_task_response_instance = CommonDataTieringTaskResponse.from_json(json)
# print the JSON string representation of the object
print(CommonDataTieringTaskResponse.to_json())

# convert the object into a dict
common_data_tiering_task_response_dict = common_data_tiering_task_response_instance.to_dict()
# create an instance of CommonDataTieringTaskResponse from a dict
common_data_tiering_task_response_from_dict = CommonDataTieringTaskResponse.from_dict(common_data_tiering_task_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


