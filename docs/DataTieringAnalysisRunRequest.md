# DataTieringAnalysisRunRequest

Specifies the request to run analysis group once.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shares** | [**List[DataTieringAnalysisShareInfo]**](DataTieringAnalysisShareInfo.md) | Specifies the list of shares to analyse. | [optional] 

## Example

```python
from cohesity_sdk.models.data_tiering_analysis_run_request import DataTieringAnalysisRunRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DataTieringAnalysisRunRequest from a JSON string
data_tiering_analysis_run_request_instance = DataTieringAnalysisRunRequest.from_json(json)
# print the JSON string representation of the object
print(DataTieringAnalysisRunRequest.to_json())

# convert the object into a dict
data_tiering_analysis_run_request_dict = data_tiering_analysis_run_request_instance.to_dict()
# create an instance of DataTieringAnalysisRunRequest from a dict
data_tiering_analysis_run_request_from_dict = DataTieringAnalysisRunRequest.from_dict(data_tiering_analysis_run_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


