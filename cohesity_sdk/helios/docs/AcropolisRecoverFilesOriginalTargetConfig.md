# AcropolisRecoverFilesOriginalTargetConfig

Specifies the configuration for recovering files and folders to the original target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_path** | **str** | Specifies the alternate path location to recover files to. | [optional] 
**recover_to_original_path** | **bool** | Specifies whether to recover files and folders to the original path location. If false, alternatePath must be specified. | 
**target_vm_credentials** | [**Credentials**](Credentials.md) | Specifies the credentials for the target VM. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.acropolis_recover_files_original_target_config import AcropolisRecoverFilesOriginalTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AcropolisRecoverFilesOriginalTargetConfig from a JSON string
acropolis_recover_files_original_target_config_instance = AcropolisRecoverFilesOriginalTargetConfig.from_json(json)
# print the JSON string representation of the object
print(AcropolisRecoverFilesOriginalTargetConfig.to_json())

# convert the object into a dict
acropolis_recover_files_original_target_config_dict = acropolis_recover_files_original_target_config_instance.to_dict()
# create an instance of AcropolisRecoverFilesOriginalTargetConfig from a dict
acropolis_recover_files_original_target_config_from_dict = AcropolisRecoverFilesOriginalTargetConfig.from_dict(acropolis_recover_files_original_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


