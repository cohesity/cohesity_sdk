# AzureRecoverFilesOriginalTargetConfig

Specifies the configuration for recovering files and folders to the original target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_path** | **str** | Specifies the alternate path location to recover files to. | [optional] 
**recover_to_original_path** | **bool** | Specifies whether to recover files and folders to the original path location. If false, alternatePath must be specified. | 
**target_vm_credentials** | [**Credentials**](Credentials.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.azure_recover_files_original_target_config import AzureRecoverFilesOriginalTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AzureRecoverFilesOriginalTargetConfig from a JSON string
azure_recover_files_original_target_config_instance = AzureRecoverFilesOriginalTargetConfig.from_json(json)
# print the JSON string representation of the object
print(AzureRecoverFilesOriginalTargetConfig.to_json())

# convert the object into a dict
azure_recover_files_original_target_config_dict = azure_recover_files_original_target_config_instance.to_dict()
# create an instance of AzureRecoverFilesOriginalTargetConfig from a dict
azure_recover_files_original_target_config_from_dict = AzureRecoverFilesOriginalTargetConfig.from_dict(azure_recover_files_original_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


