# AnalysisTaskInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **str** | Id of that particular Analysis Task. | [optional] 
**name** | **str** | Name of the Analysis task. | [optional] 
**start_time_usecs** | **str** | Denotes the start time of the tieringtask, needed for deeplinking. | [optional] 
**task_id** | **str** | Id of the Analysis task. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.analysis_task_info import AnalysisTaskInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisTaskInfo from a JSON string
analysis_task_info_instance = AnalysisTaskInfo.from_json(json)
# print the JSON string representation of the object
print(AnalysisTaskInfo.to_json())

# convert the object into a dict
analysis_task_info_dict = analysis_task_info_instance.to_dict()
# create an instance of AnalysisTaskInfo from a dict
analysis_task_info_from_dict = AnalysisTaskInfo.from_dict(analysis_task_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


