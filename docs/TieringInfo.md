# TieringInfo

Specifies the data tiering task details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**progress** | [**ProgressSummary**](ProgressSummary.md) |  | [optional] 
**stats** | [**DataTieringTaskStats**](DataTieringTaskStats.md) |  | [optional] 
**status** | **str** | Status of the analysis run. &#39;Running&#39; indicates that the run is still running. &#39;Canceled&#39; indicates that the run has been canceled. &#39;Canceling&#39; indicates that the run is in the process of being  canceled. &#39;Failed&#39; indicates that the run has failed. &#39;Missed&#39; indicates that the run was unable to take place at the  scheduled time because the previous run was still happening. &#39;Succeeded&#39; indicates that the run has finished successfully. &#39;SucceededWithWarning&#39; indicates that the run finished  successfully, but there were some warning messages. &#39;OnHold&#39; indicates that the run has On hold. &#39;Skipped&#39; indicates that the run was skipped. | [optional] 

## Example

```python
from cohesity_sdk.models.tiering_info import TieringInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TieringInfo from a JSON string
tiering_info_instance = TieringInfo.from_json(json)
# print the JSON string representation of the object
print(TieringInfo.to_json())

# convert the object into a dict
tiering_info_dict = tiering_info_instance.to_dict()
# create an instance of TieringInfo from a dict
tiering_info_from_dict = TieringInfo.from_dict(tiering_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


