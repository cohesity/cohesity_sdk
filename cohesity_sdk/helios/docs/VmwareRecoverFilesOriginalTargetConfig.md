# VmwareRecoverFilesOriginalTargetConfig

Specifies the configuration for recovering files and folders to the original target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_path** | **str** | Specifies the alternate path location to recover files to. | [optional] 
**recover_method** | **str** | Specifies the method to recover files and folders. | 
**recover_to_original_path** | **bool** | Specifies whether to recover files and folders to the original path location. If false, alternatePath must be specified. | 
**target_vm_credentials** | [**Credentials**](Credentials.md) | Specifies the credentials for the target VM. This is mandatory if the recoverMethod is AutoDeploy or UseHypervisorApis. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.vmware_recover_files_original_target_config import VmwareRecoverFilesOriginalTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareRecoverFilesOriginalTargetConfig from a JSON string
vmware_recover_files_original_target_config_instance = VmwareRecoverFilesOriginalTargetConfig.from_json(json)
# print the JSON string representation of the object
print(VmwareRecoverFilesOriginalTargetConfig.to_json())

# convert the object into a dict
vmware_recover_files_original_target_config_dict = vmware_recover_files_original_target_config_instance.to_dict()
# create an instance of VmwareRecoverFilesOriginalTargetConfig from a dict
vmware_recover_files_original_target_config_from_dict = VmwareRecoverFilesOriginalTargetConfig.from_dict(vmware_recover_files_original_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


