# DataTieringAnalysisShareInfo

Specifies the info for a particular share.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**share_id** | **int** | Specifies the id of the share. | 

## Example

```python
from cohesity_sdk.cluster.models.data_tiering_analysis_share_info import DataTieringAnalysisShareInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataTieringAnalysisShareInfo from a JSON string
data_tiering_analysis_share_info_instance = DataTieringAnalysisShareInfo.from_json(json)
# print the JSON string representation of the object
print(DataTieringAnalysisShareInfo.to_json())

# convert the object into a dict
data_tiering_analysis_share_info_dict = data_tiering_analysis_share_info_instance.to_dict()
# create an instance of DataTieringAnalysisShareInfo from a dict
data_tiering_analysis_share_info_from_dict = DataTieringAnalysisShareInfo.from_dict(data_tiering_analysis_share_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


