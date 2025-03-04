# VmwareObjectEnableSqlProtectionParams

Specifies the parameters for enabling SQL protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**VmwareSQLCredentialParams**](VmwareSQLCredentialParams.md) |  | [optional] 
**use_installed_agent** | **bool** | Specifies if agent is already installed. | [optional] 

## Example

```python
from cohesity_sdk.models.vmware_object_enable_sql_protection_params import VmwareObjectEnableSqlProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareObjectEnableSqlProtectionParams from a JSON string
vmware_object_enable_sql_protection_params_instance = VmwareObjectEnableSqlProtectionParams.from_json(json)
# print the JSON string representation of the object
print(VmwareObjectEnableSqlProtectionParams.to_json())

# convert the object into a dict
vmware_object_enable_sql_protection_params_dict = vmware_object_enable_sql_protection_params_instance.to_dict()
# create an instance of VmwareObjectEnableSqlProtectionParams from a dict
vmware_object_enable_sql_protection_params_from_dict = VmwareObjectEnableSqlProtectionParams.from_dict(vmware_object_enable_sql_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


