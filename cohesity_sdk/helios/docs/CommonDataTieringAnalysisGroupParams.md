# CommonDataTieringAnalysisGroupParams

Specifies the data tiering analysis group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the name of the data tiering analysis group. | 
**schedule** | [**DataTieringSchedule**](DataTieringSchedule.md) |  | [optional] 
**source** | [**DataTieringSource**](DataTieringSource.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.common_data_tiering_analysis_group_params import CommonDataTieringAnalysisGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonDataTieringAnalysisGroupParams from a JSON string
common_data_tiering_analysis_group_params_instance = CommonDataTieringAnalysisGroupParams.from_json(json)
# print the JSON string representation of the object
print(CommonDataTieringAnalysisGroupParams.to_json())

# convert the object into a dict
common_data_tiering_analysis_group_params_dict = common_data_tiering_analysis_group_params_instance.to_dict()
# create an instance of CommonDataTieringAnalysisGroupParams from a dict
common_data_tiering_analysis_group_params_from_dict = CommonDataTieringAnalysisGroupParams.from_dict(common_data_tiering_analysis_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


