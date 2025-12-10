# DataTieringAnalysisGroupRuns

Specifies the runs of a data tiering analysis group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_response_truncated** | **bool** | Indicates whether the result is truncated due to hitting maximum size limit | [optional] 
**runs** | [**List[DataTieringAnalysisGroupRun]**](DataTieringAnalysisGroupRun.md) | Specifies the data tiering analysis group runs. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.data_tiering_analysis_group_runs import DataTieringAnalysisGroupRuns

# TODO update the JSON string below
json = "{}"
# create an instance of DataTieringAnalysisGroupRuns from a JSON string
data_tiering_analysis_group_runs_instance = DataTieringAnalysisGroupRuns.from_json(json)
# print the JSON string representation of the object
print(DataTieringAnalysisGroupRuns.to_json())

# convert the object into a dict
data_tiering_analysis_group_runs_dict = data_tiering_analysis_group_runs_instance.to_dict()
# create an instance of DataTieringAnalysisGroupRuns from a dict
data_tiering_analysis_group_runs_from_dict = DataTieringAnalysisGroupRuns.from_dict(data_tiering_analysis_group_runs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


