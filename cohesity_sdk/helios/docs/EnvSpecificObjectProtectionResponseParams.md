# EnvSpecificObjectProtectionResponseParams

Specifies the parameters which are specific to adapter identified by enviournment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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

## Example

```python
from cohesity_sdk.helios.models.env_specific_object_protection_response_params import EnvSpecificObjectProtectionResponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of EnvSpecificObjectProtectionResponseParams from a JSON string
env_specific_object_protection_response_params_instance = EnvSpecificObjectProtectionResponseParams.from_json(json)
# print the JSON string representation of the object
print(EnvSpecificObjectProtectionResponseParams.to_json())

# convert the object into a dict
env_specific_object_protection_response_params_dict = env_specific_object_protection_response_params_instance.to_dict()
# create an instance of EnvSpecificObjectProtectionResponseParams from a dict
env_specific_object_protection_response_params_from_dict = EnvSpecificObjectProtectionResponseParams.from_dict(env_specific_object_protection_response_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


