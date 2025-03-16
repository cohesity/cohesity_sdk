# DataTieringTaskRun

Specifies the data tiering task run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time_usecs** | **int** | Specifies the end time of task run in Unix epoch Timestamp(in microseconds). | [optional] 
**id** | **str** | Specifies the id of the data tiering task run. | [optional] 
**start_time_usecs** | **int** | Specifies the start time of task run in Unix epoch Timestamp(in microseconds). | [optional] 
**tiering_info** | [**TieringInfo**](TieringInfo.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.data_tiering_task_run import DataTieringTaskRun

# TODO update the JSON string below
json = "{}"
# create an instance of DataTieringTaskRun from a JSON string
data_tiering_task_run_instance = DataTieringTaskRun.from_json(json)
# print the JSON string representation of the object
print(DataTieringTaskRun.to_json())

# convert the object into a dict
data_tiering_task_run_dict = data_tiering_task_run_instance.to_dict()
# create an instance of DataTieringTaskRun from a dict
data_tiering_task_run_from_dict = DataTieringTaskRun.from_dict(data_tiering_task_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


