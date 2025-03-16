# EnvSpecificObjectProtectionRequestParams

Specifies the parameters which are specific to adapter identified by environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | Specifies the environment for current object. | [optional] 
**aws_params** | [**AwsObjectProtectionRequestParams**](AwsObjectProtectionRequestParams.md) |  | [optional] 
**azure_params** | [**AzureObjectProtectionRequestParams**](AzureObjectProtectionRequestParams.md) |  | [optional] 
**elastifile_params** | [**ElastifileObjectProtectionRequestParams**](ElastifileObjectProtectionRequestParams.md) |  | [optional] 
**flashblade_params** | [**FlashbladeObjectProtectionRequestParams**](FlashbladeObjectProtectionRequestParams.md) |  | [optional] 
**generic_nas_params** | [**GenericNasObjectProtectionRequestParams**](GenericNasObjectProtectionRequestParams.md) |  | [optional] 
**gpfs_params** | [**GpfsObjectProtectionRequestParams**](GpfsObjectProtectionRequestParams.md) |  | [optional] 
**hyperv_params** | [**HyperVObjectProtectionRequestParams**](HyperVObjectProtectionRequestParams.md) |  | [optional] 
**isilon_params** | [**IsilonObjectProtectionRequestParams**](IsilonObjectProtectionRequestParams.md) |  | [optional] 
**mssql_params** | [**MssqlObjectProtectionRequestParams**](MssqlObjectProtectionRequestParams.md) |  | [optional] 
**netapp_params** | [**NetappObjectProtectionRequestParams**](NetappObjectProtectionRequestParams.md) |  | [optional] 
**office365_params** | [**Office365ObjectProtectionRequestParams**](Office365ObjectProtectionRequestParams.md) |  | [optional] 
**oracle_params** | [**OracleObjectProtectionRequestParams**](OracleObjectProtectionRequestParams.md) |  | [optional] 
**physical_params** | [**PhysicalObjectProtectionRequestParams**](PhysicalObjectProtectionRequestParams.md) |  | [optional] 
**sfdc_params** | [**SfdcObjectProtectionRequestParams**](SfdcObjectProtectionRequestParams.md) |  | [optional] 
**uda_params** | [**UdaObjectProtectionRequestParams**](UdaObjectProtectionRequestParams.md) |  | [optional] 
**vmware_params** | [**VmwareObjectProtectionRequestParams**](VmwareObjectProtectionRequestParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.env_specific_object_protection_request_params import EnvSpecificObjectProtectionRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of EnvSpecificObjectProtectionRequestParams from a JSON string
env_specific_object_protection_request_params_instance = EnvSpecificObjectProtectionRequestParams.from_json(json)
# print the JSON string representation of the object
print(EnvSpecificObjectProtectionRequestParams.to_json())

# convert the object into a dict
env_specific_object_protection_request_params_dict = env_specific_object_protection_request_params_instance.to_dict()
# create an instance of EnvSpecificObjectProtectionRequestParams from a dict
env_specific_object_protection_request_params_from_dict = EnvSpecificObjectProtectionRequestParams.from_dict(env_specific_object_protection_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


