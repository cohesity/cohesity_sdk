# VmwareObjectEnableAppProtectionParams

Specifies the parameters to enable app protection on VMware.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_type** | **str** | Specifies the app from which protection must be enabled. | 
**enable_sql_protection_params** | [**VmwareObjectEnableSqlProtectionParams**](VmwareObjectEnableSqlProtectionParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.vmware_object_enable_app_protection_params import VmwareObjectEnableAppProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareObjectEnableAppProtectionParams from a JSON string
vmware_object_enable_app_protection_params_instance = VmwareObjectEnableAppProtectionParams.from_json(json)
# print the JSON string representation of the object
print(VmwareObjectEnableAppProtectionParams.to_json())

# convert the object into a dict
vmware_object_enable_app_protection_params_dict = vmware_object_enable_app_protection_params_instance.to_dict()
# create an instance of VmwareObjectEnableAppProtectionParams from a dict
vmware_object_enable_app_protection_params_from_dict = VmwareObjectEnableAppProtectionParams.from_dict(vmware_object_enable_app_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


