# CommonProtectionGroupResponseParams1adf5af12d9e4081A117De198444a79bSfdcProtectionGroupParamsWrapper


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Specifies the ID of the Protection Group. | [optional] 
**name** | **str, none_type** | Specifies the name of the Protection Group. | [optional] 
**cluster_id** | **str, none_type** | Specifies the cluster ID. | [optional] 
**region_id** | **str, none_type** | Specifies the region ID. | [optional] 
**policy_id** | **str, none_type** | Specifies the unique id of the Protection Policy associated with the Protection Group. The Policy provides retry settings Protection Schedules, Priority, SLA, etc. | [optional] 
**priority** | **str, none_type** | Specifies the priority of the Protection Group. | [optional] 
**storage_domain_id** | **int, none_type** | Specifies the Storage Domain (View Box) ID where this Protection Group writes data. | [optional] 
**description** | **str, none_type** | Specifies a description of the Protection Group. | [optional] 
**start_time** | [**TimeOfDay**](TimeOfDay.md) |  | [optional] 
**end_time_usecs** | **int, none_type** | Specifies the end time in micro seconds for this Protection Group. If this is not specified, the Protection Group won&#39;t be ended. | [optional] 
**alert_policy** | [**ProtectionGroupAlertingPolicy**](ProtectionGroupAlertingPolicy.md) |  | [optional] 
**sla** | [**[SlaRule], none_type**](SlaRule.md) | Specifies the SLA parameters for this Protection Group. | [optional] 
**qos_policy** | **str, none_type** | Specifies whether the Protection Group will be written to HDD or SSD. | [optional] 
**abort_in_blackouts** | **bool, none_type** | Specifies whether currently executing jobs should abort if a blackout period specified by a policy starts. Available only if the selected policy has at least one blackout period. Default value is false. | [optional] 
**pause_in_blackouts** | **bool, none_type** | Specifies whether currently executing jobs should be paused if a blackout period specified by a policy starts. Available only if the selected policy has at least one blackout period. Default value is false. This field should not be set to true if &#39;abortInBlackouts&#39; is sent as true. | [optional] 
**is_active** | **bool, none_type** | Specifies if the Protection Group is active or not. | [optional] 
**is_deleted** | **bool, none_type** | Specifies if the Protection Group has been deleted. | [optional] 
**is_paused** | **bool, none_type** | Specifies if the the Protection Group is paused. New runs are not scheduled for the paused Protection Groups. Active run if any is not impacted. | [optional] 
**environment** | **str, none_type** | Specifies the environment of the Protection Group. | [optional] 
**last_run** | [**ProtectionGroupRun**](ProtectionGroupRun.md) |  | [optional] 
**permissions** | [**[Tenant], none_type**](Tenant.md) | Specifies the list of tenants that have permissions for this protection group. | [optional] 
**is_protect_once** | **bool, none_type** | Specifies if the the Protection Group is using a protect once type of policy. This field is helpful to identify run happen for this group. | [optional] 
**missing_entities** | [**[MissingEntityParams], none_type**](MissingEntityParams.md) | Specifies the Information about missing entities. | [optional] 
**num_protected_objects** | **int, none_type** | Specifies the number of protected objects of the Protection Group. | [optional] 
**sfdc_params** | [**SfdcProtectionGroupParams**](SfdcProtectionGroupParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


