# CommonProtectionGroupRequestParams2384072a0e0849d28bd538044d7ffd40GenericNasProtectionGroupParamsWrapper


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the name of the Protection Group. | 
**policy_id** | **str, none_type** | Specifies the unique id of the Protection Policy associated with the Protection Group. The Policy provides retry settings Protection Schedules, Priority, SLA, etc. | 
**environment** | **str, none_type** | Specifies the environment type of the Protection Group. | 
**priority** | **str, none_type** | Specifies the priority of the Protection Group. | [optional] 
**storage_domain_id** | **int, none_type** | Specifies the Storage Domain (View Box) ID where this Protection Group writes data. | [optional] 
**description** | **str, none_type** | Specifies a description of the Protection Group. | [optional] 
**start_time** | [**TimeOfDay**](TimeOfDay.md) |  | [optional] 
**end_time_usecs** | **int, none_type** | Specifies the end time in micro seconds for this Protection Group. If this is not specified, the Protection Group won&#39;t be ended. | [optional] 
**alert_policy** | [**ProtectionGroupAlertingPolicy**](ProtectionGroupAlertingPolicy.md) |  | [optional] 
**sla** | [**[SlaRule], none_type**](SlaRule.md) | Specifies the SLA parameters for this Protection Group. | [optional] 
**qos_policy** | **str, none_type** | Specifies whether the Protection Group will be written to HDD or SSD. | [optional] 
**abort_in_blackouts** | **bool, none_type** | Specifies whether currently executing jobs should abort if a blackout period specified by a policy starts. Available only if the selected policy has at least one blackout period. Default value is false. | [optional] 
**is_paused** | **bool, none_type** | Specifies if the the Protection Group is paused. New runs are not scheduled for the paused Protection Groups. Active run if any is not impacted. | [optional] 
**generic_nas_params** | [**GenericNasProtectionGroupParams**](GenericNasProtectionGroupParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


