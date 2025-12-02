# TieringTaskInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **str** | Id of that particular Tiering Task. | [optional] 
**name** | **str** | Name of the Tiering task. | [optional] 
**start_time_usecs** | **str** | Denotes the start time of the tieringtask, needed for deeplinking. | [optional] 
**task_id** | **str** | Id of the Tiering task. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.tiering_task_info import TieringTaskInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TieringTaskInfo from a JSON string
tiering_task_info_instance = TieringTaskInfo.from_json(json)
# print the JSON string representation of the object
print(TieringTaskInfo.to_json())

# convert the object into a dict
tiering_task_info_dict = tiering_task_info_instance.to_dict()
# create an instance of TieringTaskInfo from a dict
tiering_task_info_from_dict = TieringTaskInfo.from_dict(tiering_task_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


