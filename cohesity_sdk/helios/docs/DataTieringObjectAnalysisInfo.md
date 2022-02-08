# DataTieringObjectAnalysisInfo

Specifies the data tiering object analysis details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str, none_type** | Status of the analysis run. &#39;Running&#39; indicates that the run  is still running. &#39;Canceled&#39; indicates that the run has been canceled.  &#39;Canceling&#39; indicates that the run is in the process of being  canceled.  &#39;Failed&#39; indicates that the run has failed. &#39;Missed&#39; indicates that the  run was unable to take place at the  scheduled time because the previous  run was still happening. &#39;Succeeded&#39; indicates that the run has finished  successfully. &#39;SucceededWithWarning&#39; indicates that the run finished   successfully, but there were some warning messages. &#39;OnHold&#39; indicates  that the run has On hold. | [optional] 
**message** | **str, none_type** | A message about the error if encountered while performing data   tiering analysis. | [optional] 
**stats** | [**[DataTieringShareStats], none_type**](DataTieringShareStats.md) | Specifies the source share analysis stats. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


