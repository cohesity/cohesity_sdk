# UpdateProtectedObjectsRequest

Specifies the request to update an object backup configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**aws_params** | [**AwsObjectProtectionUpdateRequestParams**](AwsObjectProtectionUpdateRequestParams.md) |  | [optional] 
**azure_params** | [**AzureObjectProtectionUpdateRequestParams**](AzureObjectProtectionUpdateRequestParams.md) |  | [optional] 
**elastifile_params** | [**ElastifileObjectProtectionUpdateRequestParams**](ElastifileObjectProtectionUpdateRequestParams.md) |  | [optional] 
**environment** | **str, none_type** | Specifies the environment for current object. | [optional] 
**flashblade_params** | [**FlashbladeObjectProtectionUpdateRequestParams**](FlashbladeObjectProtectionUpdateRequestParams.md) |  | [optional] 
**generic_nas_params** | [**GenericNasObjectProtectionUpdateRequestParams**](GenericNasObjectProtectionUpdateRequestParams.md) |  | [optional] 
**gpfs_params** | [**GpfsObjectProtectionUpdateRequestParams**](GpfsObjectProtectionUpdateRequestParams.md) |  | [optional] 
**hyperv_params** | [**HyperVObjectProtectionUpdateRequestParams**](HyperVObjectProtectionUpdateRequestParams.md) |  | [optional] 
**isilon_params** | [**IsilonObjectProtectionUpdateRequestParams**](IsilonObjectProtectionUpdateRequestParams.md) |  | [optional] 
**mssql_params** | [**CommonMssqlObjectProtectionParams**](CommonMssqlObjectProtectionParams.md) |  | [optional] 
**netapp_params** | [**NetappObjectProtectionUpdateRequestParams**](NetappObjectProtectionUpdateRequestParams.md) |  | [optional] 
**office365_params** | [**Office365ObjectProtectionParams**](Office365ObjectProtectionParams.md) |  | [optional] 
**oracle_params** | [**OracleObjectBasedProtectionParams**](OracleObjectBasedProtectionParams.md) |  | [optional] 
**physical_params** | [**PhysicalObjectProtectionParams**](PhysicalObjectProtectionParams.md) |  | [optional] 
**sfdc_params** | [**SfdcObjectProtectionParams**](SfdcObjectProtectionParams.md) |  | [optional] 
**uda_params** | [**UdaObjectProtectionParams**](UdaObjectProtectionParams.md) |  | [optional] 
**vmware_params** | [**VmwareObjectProtectionUpdateRequestParams**](VmwareObjectProtectionUpdateRequestParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


