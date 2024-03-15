# MaintenanceModeConfig

Specifies the entity metadata for maintenance mode.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_time_intervals** | [**[TimeRangeUsecs]**](TimeRangeUsecs.md) | Specifies the absolute intervals where the maintenance schedule is valid, i.e. maintenance_shedule is considered only for these time ranges. (For example, if there is one time range with [now_usecs, now_usecs + 10 days], the action will be done during the maintenance_schedule for the next 10 days.)The start time must be specified. The end time can be -1 which would denote an indefinite maintenance mode. | [optional] 
**maintenance_schedule** | [**Schedule**](Schedule.md) |  | [optional] 
**user_message** | **str** | User provided message associated with this maintenance mode. | [optional] 
**workflow_intervention_spec_list** | [**[WorkflowInterventionSpec]**](WorkflowInterventionSpec.md) | Specifies the type of intervention for different workflows when the source goes into maintenance mode. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


