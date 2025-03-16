# ProtectedObjectBackupConfig

Specifies the backup configuration for protected object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abort_in_blackouts** | **bool** | Specifies whether currently executing object backup should abort if a blackout period specified by a policy starts. Available only if the selected policy has at least one blackout period. Default value is false. | [optional] 
**end_time_usecs** | **int** | Specifies the end time in micro seconds for this Protection Group. If this is not specified, the Protection Group won&#39;t be ended. | [optional] 
**policy_config** | [**PolicyConfig**](PolicyConfig.md) |  | [optional] 
**policy_id** | **str** | Specifies the unique id of the Protection Policy. The Policy settings will be attached with every object and will be used in backup. | [optional] 
**priority** | **str** | Specifies the priority for the objects backup. | [optional] 
**qos_policy** | **str** | Specifies whether object backup will be written to HDD or SSD. | [optional] 
**skip_rigel_for_backup** | **bool** | Specifies whether to skip Rigel for backup or not. | [optional] 
**sla** | [**List[SlaRule]**](SlaRule.md) | Specifies the SLA parameters for list of objects. | [optional] 
**start_time** | [**TimeOfDay**](TimeOfDay.md) |  | [optional] 
**storage_domain_id** | **int** | Specifies the Storage Domain (View Box) ID where the object backup will be taken. This is not required if Cloud archive direct is benig used. | [optional] 
**aws_params** | [**AwsObjectProtectionResponseParams**](AwsObjectProtectionResponseParams.md) |  | [optional] 
**azure_params** | [**AzureObjectProtectionResponseParams**](AzureObjectProtectionResponseParams.md) |  | [optional] 
**elastifile_params** | [**ElastifileObjectProtectionResponseParams**](ElastifileObjectProtectionResponseParams.md) |  | [optional] 
**environment** | **str** | Specifies the environment for current object. | [optional] 
**flashblade_params** | [**FlashbladeObjectProtectionResponseParams**](FlashbladeObjectProtectionResponseParams.md) |  | [optional] 
**generic_nas_params** | [**GenericNasObjectProtectionResponseParams**](GenericNasObjectProtectionResponseParams.md) |  | [optional] 
**gpfs_params** | [**GpfsObjectProtectionResponseParams**](GpfsObjectProtectionResponseParams.md) |  | [optional] 
**hyperv_params** | [**HyperVObjectProtectionResponseParams**](HyperVObjectProtectionResponseParams.md) |  | [optional] 
**isilon_params** | [**IsilonObjectProtectionResponseParams**](IsilonObjectProtectionResponseParams.md) |  | [optional] 
**mssql_params** | [**MssqlObjectProtectionResponseParams**](MssqlObjectProtectionResponseParams.md) |  | [optional] 
**netapp_params** | [**NetappObjectProtectionResponseParams**](NetappObjectProtectionResponseParams.md) |  | [optional] 
**office365_params** | [**Office365ObjectProtectionResponseParams**](Office365ObjectProtectionResponseParams.md) |  | [optional] 
**oracle_params** | [**OracleObjectProtectionResponseParams**](OracleObjectProtectionResponseParams.md) |  | [optional] 
**physical_params** | [**PhysicalObjectProtectionResponseParams**](PhysicalObjectProtectionResponseParams.md) |  | [optional] 
**sfdc_params** | [**SfdcObjectProtectionResponseParams**](SfdcObjectProtectionResponseParams.md) |  | [optional] 
**uda_params** | [**UdaObjectProtectionResponseParams**](UdaObjectProtectionResponseParams.md) |  | [optional] 
**vmware_params** | [**VmwareObjectProtectionResponseParams**](VmwareObjectProtectionResponseParams.md) |  | [optional] 
**auto_protect_parent_id** | **int** | Specifies the parent ID of the object which the backup configuration is applied to if this is an auto protect config. | [optional] 
**is_active** | **bool** | Specifies whether or not protection has been deactivated on this object. | [optional] 
**is_auto_protect_config** | **bool** | Specifies whether or not this configuration is applied to an autoprotected object rather than this specific object. | [optional] 
**is_paused** | **bool** | Specifies whether or not protection has been paused on this object. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.protected_object_backup_config import ProtectedObjectBackupConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectedObjectBackupConfig from a JSON string
protected_object_backup_config_instance = ProtectedObjectBackupConfig.from_json(json)
# print the JSON string representation of the object
print(ProtectedObjectBackupConfig.to_json())

# convert the object into a dict
protected_object_backup_config_dict = protected_object_backup_config_instance.to_dict()
# create an instance of ProtectedObjectBackupConfig from a dict
protected_object_backup_config_from_dict = ProtectedObjectBackupConfig.from_dict(protected_object_backup_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


