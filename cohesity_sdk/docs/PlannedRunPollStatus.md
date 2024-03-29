# PlannedRunPollStatus

Specifies whether run has been scheduled or not and also returns the unique run id along with failoverId upon scheduling the run.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failover_id** | **str, none_type** | Specifies the unique failover Id which will be generated by orchestrator. This Id will be used to uniquely identify current failover operation. | [optional] 
**waiting_on_other_run_cancellations** | **bool, none_type** | If cancelNonFailoverRuns was passed as true during creation of run for current failover then this will return the status of other run cacellations. If other runs are still pending for cancellations then this will be returned as true otherwise it will be return as false. | [optional] 
**run_id** | **str, none_type** | If run has been scheduled then this field will be populated with unique run id. | [optional] 
**protection_group_id** | **str, none_type** | Specifies the protection group id to which this run belongs. | [optional] 
**backup_task_status** | **str, none_type** | Status of the backup job. &#39;Running&#39; indicates that the run is still running. &#39;Canceled&#39; indicates that the run has been canceled. &#39;Canceling&#39; indicates that the run is in the process of being canceled. &#39;Paused&#39; indicates that the ongoing run has been paused. &#39;Failed&#39; indicates that the run has failed. &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening. &#39;Succeeded&#39; indicates that the run has finished successfully. &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages. &#39;Skipped&#39; indicates that the run was skipped. | [optional] 
**on_prem_deploy_task_status** | **str, none_type** | Status of the OnPrem deploy task. &#39;Running&#39; indicates that the run is still running. &#39;Canceled&#39; indicates that the run has been canceled. &#39;Canceling&#39; indicates that the run is in the process of being canceled. &#39;Paused&#39; indicates that the ongoing run has been paused. &#39;Failed&#39; indicates that the run has failed. &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening. &#39;Succeeded&#39; indicates that the run has finished successfully. &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages. &#39;Skipped&#39; indicates that the run was skipped. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


