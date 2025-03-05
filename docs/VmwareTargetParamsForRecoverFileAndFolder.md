# VmwareTargetParamsForRecoverFileAndFolder

Specifies the parameters for a VMware recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool** | Specifies whether to continue recovering other files if one of files or folders failed to recover. Default value is false. | [optional] 
**new_target_config** | [**VmwareRecoverFilesNewTargetConfig**](VmwareRecoverFilesNewTargetConfig.md) |  | [optional] 
**original_target_config** | [**VmwareRecoverFilesOriginalTargetConfig**](VmwareRecoverFilesOriginalTargetConfig.md) |  | [optional] 
**overwrite_existing** | **bool** | Specifies whether to overwrite the existing files. Default is true. | [optional] 
**preserve_attributes** | **bool** | Specifies whether to preserve original attributes. Default is true. | [optional] 
**recover_to_original_target** | **bool** | Specifies whether to recover to the original target. If true, originalTargetConfig must be specified. If false, newTargetConfig must be specified. | 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.vmware_target_params_for_recover_file_and_folder import VmwareTargetParamsForRecoverFileAndFolder

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareTargetParamsForRecoverFileAndFolder from a JSON string
vmware_target_params_for_recover_file_and_folder_instance = VmwareTargetParamsForRecoverFileAndFolder.from_json(json)
# print the JSON string representation of the object
print(VmwareTargetParamsForRecoverFileAndFolder.to_json())

# convert the object into a dict
vmware_target_params_for_recover_file_and_folder_dict = vmware_target_params_for_recover_file_and_folder_instance.to_dict()
# create an instance of VmwareTargetParamsForRecoverFileAndFolder from a dict
vmware_target_params_for_recover_file_and_folder_from_dict = VmwareTargetParamsForRecoverFileAndFolder.from_dict(vmware_target_params_for_recover_file_and_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


