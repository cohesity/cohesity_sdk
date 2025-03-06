# UpdateProtectedObjectsRequest

Specifies the request to update an object backup configuration.

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
**aws_params** | [**AwsObjectProtectionUpdateRequestParams**](AwsObjectProtectionUpdateRequestParams.md) |  | [optional] 
**azure_params** | [**AzureObjectProtectionUpdateRequestParams**](AzureObjectProtectionUpdateRequestParams.md) |  | [optional] 
**elastifile_params** | [**ElastifileObjectProtectionUpdateRequestParams**](ElastifileObjectProtectionUpdateRequestParams.md) |  | [optional] 
**environment** | **str** | Specifies the environment for current object. | [optional] 
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

## Example

```python
from cohesity_sdk.cluster.models.update_protected_objects_request import UpdateProtectedObjectsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProtectedObjectsRequest from a JSON string
update_protected_objects_request_instance = UpdateProtectedObjectsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateProtectedObjectsRequest.to_json())

# convert the object into a dict
update_protected_objects_request_dict = update_protected_objects_request_instance.to_dict()
# create an instance of UpdateProtectedObjectsRequest from a dict
update_protected_objects_request_from_dict = UpdateProtectedObjectsRequest.from_dict(update_protected_objects_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


