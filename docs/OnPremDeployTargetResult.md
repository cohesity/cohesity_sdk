# OnPremDeployTargetResult

OnPrem Deploy result for a target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | Target environment of the onprem deploy task. | [optional] 
**error_message** | **str** | Specifies the error message for onprem task failure. | [optional] 
**message** | **str** | Message about the onprem deploy run. | [optional] 
**status** | **str** | Status of the OnPrem deploy for a target. &#39;Running&#39; indicates that the run is still running. &#39;Canceled&#39; indicates that the run has been canceled. &#39;Canceling&#39; indicates that the run is in the process of being canceled. &#39;Paused&#39; indicates that the ongoing run has been paused. &#39;Failed&#39; indicates that the run has failed. &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening. &#39;Succeeded&#39; indicates that the run has finished successfully. &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages. &#39;Skipped&#39; indicates that the run was skipped. | [optional] 
**vmware_params** | [**OnPremDeployTargetResultVmwareParams**](OnPremDeployTargetResultVmwareParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.on_prem_deploy_target_result import OnPremDeployTargetResult

# TODO update the JSON string below
json = "{}"
# create an instance of OnPremDeployTargetResult from a JSON string
on_prem_deploy_target_result_instance = OnPremDeployTargetResult.from_json(json)
# print the JSON string representation of the object
print(OnPremDeployTargetResult.to_json())

# convert the object into a dict
on_prem_deploy_target_result_dict = on_prem_deploy_target_result_instance.to_dict()
# create an instance of OnPremDeployTargetResult from a dict
on_prem_deploy_target_result_from_dict = OnPremDeployTargetResult.from_dict(on_prem_deploy_target_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


