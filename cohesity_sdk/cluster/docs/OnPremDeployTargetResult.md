# OnPremDeployTargetResult

OnPrem Deploy result for a target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str, none_type** | Target environment of the onprem deploy task. | [optional]  if omitted the server will use the default value of "kVMware"
**error_message** | **str, none_type** | Specifies the error message for onprem task failure. | [optional] 
**message** | **str, none_type** | Message about the onprem deploy run. | [optional] 
**status** | **str, none_type** | Status of the OnPrem deploy for a target. &#39;Running&#39; indicates that the run is still running. &#39;Canceled&#39; indicates that the run has been canceled. &#39;Canceling&#39; indicates that the run is in the process of being canceled. &#39;Paused&#39; indicates that the ongoing run has been paused. &#39;Failed&#39; indicates that the run has failed. &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening. &#39;Succeeded&#39; indicates that the run has finished successfully. &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages. | [optional] 
**vmware_params** | [**OnPremDeployTargetResultVmwareParams**](OnPremDeployTargetResultVmwareParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


