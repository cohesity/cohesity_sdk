# VmwareRecoverFilesNewTargetConfig

Specifies the configuration for recovering files and folders to a new target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**absolute_path** | **str** | Specifies the path location to recover files to. | 
**recover_method** | **str** | Specifies the method to recover files and folders. | 
**target_vm** | [**RecoverTarget**](RecoverTarget.md) |  | 
**target_vm_credentials** | [**Credentials**](Credentials.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.vmware_recover_files_new_target_config import VmwareRecoverFilesNewTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareRecoverFilesNewTargetConfig from a JSON string
vmware_recover_files_new_target_config_instance = VmwareRecoverFilesNewTargetConfig.from_json(json)
# print the JSON string representation of the object
print(VmwareRecoverFilesNewTargetConfig.to_json())

# convert the object into a dict
vmware_recover_files_new_target_config_dict = vmware_recover_files_new_target_config_instance.to_dict()
# create an instance of VmwareRecoverFilesNewTargetConfig from a dict
vmware_recover_files_new_target_config_from_dict = VmwareRecoverFilesNewTargetConfig.from_dict(vmware_recover_files_new_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


