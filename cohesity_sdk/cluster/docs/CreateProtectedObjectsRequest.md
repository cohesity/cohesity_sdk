# CreateProtectedObjectsRequest

Specifies the request for creating an object backup.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[EnvSpecificObjectProtectionRequestParams], none_type**](EnvSpecificObjectProtectionRequestParams.md) | Specifies the list of objects to be protected. Multiple objects from different adapters can be provided as input. | 
**activate_remote_object_protection** | **bool, none_type** | If set to true, it will look for the remote backup of the given user and object, and activates it. Creates a new backup if the remote backup is not found. After activation, this object cannot get snapshots from remote clusters. | [optional] 
**is_paused** | **bool, none_type** | If set to true, then the object specs will be created in the paused state preventing any runs from happening until they are unpaused. | [optional] 
**abort_in_blackouts** | **bool, none_type** | Specifies whether currently executing object backup should abort if a blackout period specified by a policy starts. Available only if the selected policy has at least one blackout period. Default value is false. | [optional] 
**end_time_usecs** | **int, none_type** | Specifies the end time in micro seconds for this Protection Group. If this is not specified, the Protection Group won&#39;t be ended. | [optional] 
**policy_config** | [**PolicyConfig**](PolicyConfig.md) |  | [optional] 
**policy_id** | **str, none_type** | Specifies the unique id of the Protection Policy. The Policy settings will be attached with every object and will be used in backup. | [optional] 
**priority** | **str, none_type** | Specifies the priority for the objects backup. | [optional] 
**qos_policy** | **str, none_type** | Specifies whether object backup will be written to HDD or SSD. | [optional] 
**skip_rigel_for_backup** | **bool, none_type** | Specifies whether to skip Rigel for backup or not. | [optional] 
**sla** | [**[SlaRule], none_type**](SlaRule.md) | Specifies the SLA parameters for list of objects. | [optional] 
**start_time** | [**TimeOfDay**](TimeOfDay.md) |  | [optional] 
**storage_domain_id** | **int, none_type** | Specifies the Storage Domain (View Box) ID where the object backup will be taken. This is not required if Cloud archive direct is benig used. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


