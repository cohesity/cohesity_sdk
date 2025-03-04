# DataTieringAnalysisGroupRun

Specifies the data tiering analysis group run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_info** | [**DataTieringAnalysisInfo**](DataTieringAnalysisInfo.md) |  | [optional] 
**end_time_usecs** | **int** | Specifies the end time of analysis run in Unix epoch Timestamp(in microseconds). | [optional] 
**id** | **str** | Specifies the ID of the data tiering analysis group run. | [optional] 
**objects** | [**List[DataTieringObjectInfo]**](DataTieringObjectInfo.md) | Specifies the objects details analyzed during data tiering analysis group run. | [optional] 
**start_time_usecs** | **int** | Specifies the start time of analysis run in Unix epoch Timestamp(in microseconds). | [optional] 

## Example

```python
from cohesity_sdk.models.data_tiering_analysis_group_run import DataTieringAnalysisGroupRun

# TODO update the JSON string below
json = "{}"
# create an instance of DataTieringAnalysisGroupRun from a JSON string
data_tiering_analysis_group_run_instance = DataTieringAnalysisGroupRun.from_json(json)
# print the JSON string representation of the object
print(DataTieringAnalysisGroupRun.to_json())

# convert the object into a dict
data_tiering_analysis_group_run_dict = data_tiering_analysis_group_run_instance.to_dict()
# create an instance of DataTieringAnalysisGroupRun from a dict
data_tiering_analysis_group_run_from_dict = DataTieringAnalysisGroupRun.from_dict(data_tiering_analysis_group_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


