# McmObjectSummaryResult

Specifies the result for mcm object summary.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregated_summary** | [**List[McmObjectSummary]**](McmObjectSummary.md) | Specifies the aggregated objects summary across clusters. | [optional] 
**objects** | [**List[McmClusterObjectSummary]**](McmClusterObjectSummary.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_object_summary_result import McmObjectSummaryResult

# TODO update the JSON string below
json = "{}"
# create an instance of McmObjectSummaryResult from a JSON string
mcm_object_summary_result_instance = McmObjectSummaryResult.from_json(json)
# print the JSON string representation of the object
print(McmObjectSummaryResult.to_json())

# convert the object into a dict
mcm_object_summary_result_dict = mcm_object_summary_result_instance.to_dict()
# create an instance of McmObjectSummaryResult from a dict
mcm_object_summary_result_from_dict = McmObjectSummaryResult.from_dict(mcm_object_summary_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


