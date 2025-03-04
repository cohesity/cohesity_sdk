# DataTieringAnalysisGroup

Specifies the data tiering analysis group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the name of the data tiering analysis group. | 
**schedule** | [**DataTieringSchedule**](DataTieringSchedule.md) |  | [optional] 
**source** | [**DataTieringSource**](DataTieringSource.md) |  | [optional] 
**id** | **str** | Specifies the ID of the data tiering analysis group. | [optional] 
**last_run** | [**DataTieringAnalysisGroupRun**](DataTieringAnalysisGroupRun.md) |  | [optional] 
**last_successful_run** | [**DataTieringAnalysisGroupRun**](DataTieringAnalysisGroupRun.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.data_tiering_analysis_group import DataTieringAnalysisGroup

# TODO update the JSON string below
json = "{}"
# create an instance of DataTieringAnalysisGroup from a JSON string
data_tiering_analysis_group_instance = DataTieringAnalysisGroup.from_json(json)
# print the JSON string representation of the object
print(DataTieringAnalysisGroup.to_json())

# convert the object into a dict
data_tiering_analysis_group_dict = data_tiering_analysis_group_instance.to_dict()
# create an instance of DataTieringAnalysisGroup from a dict
data_tiering_analysis_group_from_dict = DataTieringAnalysisGroup.from_dict(data_tiering_analysis_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


