# EnvSpecificObjectProtectionUpdateRequestParams

Specifies the update parameters which are specific to adapter identified by enviournment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from cohesity_sdk.cluster.models.env_specific_object_protection_update_request_params import EnvSpecificObjectProtectionUpdateRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of EnvSpecificObjectProtectionUpdateRequestParams from a JSON string
env_specific_object_protection_update_request_params_instance = EnvSpecificObjectProtectionUpdateRequestParams.from_json(json)
# print the JSON string representation of the object
print(EnvSpecificObjectProtectionUpdateRequestParams.to_json())

# convert the object into a dict
env_specific_object_protection_update_request_params_dict = env_specific_object_protection_update_request_params_instance.to_dict()
# create an instance of EnvSpecificObjectProtectionUpdateRequestParams from a dict
env_specific_object_protection_update_request_params_from_dict = EnvSpecificObjectProtectionUpdateRequestParams.from_dict(env_specific_object_protection_update_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


