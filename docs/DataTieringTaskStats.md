# DataTieringTaskStats

Specifies the stats of data tiering task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes_read** | **int** | Specifies total logical bytes read for creating the snapshot. | [optional] 
**bytes_written** | **int** | Specifies total size of data in bytes written after taking backup. | [optional] 
**logical_size_bytes** | **int** | Specifies total logical size of object(s) in bytes. | [optional] 
**changed_entity_count** | **int** | Specifies changed entity count. | [optional] 
**entity_count** | **int** | Specifies total entity count. | [optional] 
**is_tiering_goal_met** | **bool** | Specifies whether tiering goal has been met. | [optional] [default to False]
**total_tiered_bytes** | **int** | Specifies total amount of data successfully tiered from the NAS source. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.data_tiering_task_stats import DataTieringTaskStats

# TODO update the JSON string below
json = "{}"
# create an instance of DataTieringTaskStats from a JSON string
data_tiering_task_stats_instance = DataTieringTaskStats.from_json(json)
# print the JSON string representation of the object
print(DataTieringTaskStats.to_json())

# convert the object into a dict
data_tiering_task_stats_dict = data_tiering_task_stats_instance.to_dict()
# create an instance of DataTieringTaskStats from a dict
data_tiering_task_stats_from_dict = DataTieringTaskStats.from_dict(data_tiering_task_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


