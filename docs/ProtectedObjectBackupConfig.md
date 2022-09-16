# ProtectedObjectBackupConfig

Specifies the backup configuration for protected object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_id** | **str, none_type** | Specifies the unique id of the Protection Policy. The Policy settings will be attached with every object and will be used in backup. | 
**storage_domain_id** | **int, none_type** | Specifies the Storage Domain (View Box) ID where the object backup will be taken. This is not required if Cloud archive direct is benig used. | [optional] 
**start_time** | [**TimeOfDay**](TimeOfDay.md) |  | [optional] 
**priority** | **str, none_type** | Specifies the priority for the objects backup. | [optional] 
**sla** | [**[SlaRule], none_type**](SlaRule.md) | Specifies the SLA parameters for list of objects. | [optional] 
**qos_policy** | **str, none_type** | Specifies whether object backup will be written to HDD or SSD. | [optional] 
**abort_in_blackouts** | **bool, none_type** | Specifies whether currently executing object backup should abort if a blackout period specified by a policy starts. Available only if the selected policy has at least one blackout period. Default value is false. | [optional] 
**environment** | **str, none_type** | Specifies the environment for current object. | [optional] 
**vmware_params** | [**VmwareObjectProtectionResponseParams**](VmwareObjectProtectionResponseParams.md) |  | [optional] 
**generic_nas_params** | [**GenericNasObjectProtectionResponseParams**](GenericNasObjectProtectionResponseParams.md) |  | [optional] 
**gpfs_params** | [**GpfsObjectProtectionResponseParams**](GpfsObjectProtectionResponseParams.md) |  | [optional] 
**elastifile_params** | [**ElastifileObjectProtectionResponseParams**](ElastifileObjectProtectionResponseParams.md) |  | [optional] 
**netapp_params** | [**NetappObjectProtectionResponseParams**](NetappObjectProtectionResponseParams.md) |  | [optional] 
**isilon_params** | [**IsilonObjectProtectionResponseParams**](IsilonObjectProtectionResponseParams.md) |  | [optional] 
**flashblade_params** | [**FlashbladeObjectProtectionResponseParams**](FlashbladeObjectProtectionResponseParams.md) |  | [optional] 
**mssql_params** | [**MssqlObjectProtectionResponseParams**](MssqlObjectProtectionResponseParams.md) |  | [optional] 
**office365_user_mailbox_params** | [**Office365UserMailboxObjectProtectionResponseParams**](Office365UserMailboxObjectProtectionResponseParams.md) |  | [optional] 
**is_auto_protect_config** | **bool, none_type** | Specifies whether or not this configuration is applied to an autoprotected object rather than this specific object. | [optional] 
**auto_protect_parent_id** | **int, none_type** | Specifies the parent ID of the object which the backup configuration is applied to if this is an auto protect config. | [optional] 
**is_paused** | **bool, none_type** | Specifies whether or not protection has been paused on this object. | [optional] 
**is_active** | **bool, none_type** | Specifies whether or not protection has been deactivated on this object. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


