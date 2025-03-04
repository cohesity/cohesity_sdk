# AzureRecoverFilesNewTargetConfig

Specifies the configuration for recovering files and folders to the new target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**absolute_path** | **str** | Specifies the absolute path location to recover files to. | 
**target_vm** | [**RecoverTarget**](RecoverTarget.md) |  | 
**target_vm_credentials** | [**Credentials**](Credentials.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.azure_recover_files_new_target_config import AzureRecoverFilesNewTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AzureRecoverFilesNewTargetConfig from a JSON string
azure_recover_files_new_target_config_instance = AzureRecoverFilesNewTargetConfig.from_json(json)
# print the JSON string representation of the object
print(AzureRecoverFilesNewTargetConfig.to_json())

# convert the object into a dict
azure_recover_files_new_target_config_dict = azure_recover_files_new_target_config_instance.to_dict()
# create an instance of AzureRecoverFilesNewTargetConfig from a dict
azure_recover_files_new_target_config_from_dict = AzureRecoverFilesNewTargetConfig.from_dict(azure_recover_files_new_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


