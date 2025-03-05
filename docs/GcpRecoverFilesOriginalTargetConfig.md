# GcpRecoverFilesOriginalTargetConfig

Specifies the configuration for recovering files and folders to the original target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_path** | **str** | Specifies the alternate path location to recover files to. | [optional] 
**recover_to_original_path** | **bool** | Specifies whether to recover files and folders to the original path location. If false, alternatePath must be specified. | 
**target_vm_credentials** | [**Credentials**](Credentials.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.gcp_recover_files_original_target_config import GcpRecoverFilesOriginalTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GcpRecoverFilesOriginalTargetConfig from a JSON string
gcp_recover_files_original_target_config_instance = GcpRecoverFilesOriginalTargetConfig.from_json(json)
# print the JSON string representation of the object
print(GcpRecoverFilesOriginalTargetConfig.to_json())

# convert the object into a dict
gcp_recover_files_original_target_config_dict = gcp_recover_files_original_target_config_instance.to_dict()
# create an instance of GcpRecoverFilesOriginalTargetConfig from a dict
gcp_recover_files_original_target_config_from_dict = GcpRecoverFilesOriginalTargetConfig.from_dict(gcp_recover_files_original_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


