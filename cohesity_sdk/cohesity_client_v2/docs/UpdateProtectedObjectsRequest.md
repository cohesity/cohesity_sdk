# UpdateProtectedObjectsRequest

Specifies the request to update an object backup configuration.

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
**vmware_params** | [**VmwareObjectProtectionUpdateRequestParams**](VmwareObjectProtectionUpdateRequestParams.md) |  | [optional] 
**generic_nas_params** | [**GenericNasObjectProtectionUpdateRequestParams**](GenericNasObjectProtectionUpdateRequestParams.md) |  | [optional] 
**gpfs_params** | [**GpfsObjectProtectionUpdateRequestParams**](GpfsObjectProtectionUpdateRequestParams.md) |  | [optional] 
**elastifile_params** | [**ElastifileObjectProtectionUpdateRequestParams**](ElastifileObjectProtectionUpdateRequestParams.md) |  | [optional] 
**netapp_params** | [**NetappObjectProtectionUpdateRequestParams**](NetappObjectProtectionUpdateRequestParams.md) |  | [optional] 
**isilon_params** | [**IsilonObjectProtectionUpdateRequestParams**](IsilonObjectProtectionUpdateRequestParams.md) |  | [optional] 
**flashblade_params** | [**FlashbladeObjectProtectionUpdateRequestParams**](FlashbladeObjectProtectionUpdateRequestParams.md) |  | [optional] 
**mssql_params** | [**MssqlObjectProtectionUpdateRequestParams**](MssqlObjectProtectionUpdateRequestParams.md) |  | [optional] 
**office365_user_mailbox_params** | [**Office365UserMailboxObjectProtectionUpdateRequestParams**](Office365UserMailboxObjectProtectionUpdateRequestParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


