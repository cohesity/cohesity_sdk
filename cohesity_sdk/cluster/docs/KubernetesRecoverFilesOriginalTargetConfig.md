# KubernetesRecoverFilesOriginalTargetConfig

Specifies the configuration for recovering files and folders to the original target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_path** | **str** | Specifies the alternate path location to recover files to. | [optional] 
**recover_to_original_path** | **bool** | Specifies whether to recover files and folders to the original path location. If false, alternatePath must be specified. | 

## Example

```python
from cohesity_sdk.cluster.models.kubernetes_recover_files_original_target_config import KubernetesRecoverFilesOriginalTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesRecoverFilesOriginalTargetConfig from a JSON string
kubernetes_recover_files_original_target_config_instance = KubernetesRecoverFilesOriginalTargetConfig.from_json(json)
# print the JSON string representation of the object
print(KubernetesRecoverFilesOriginalTargetConfig.to_json())

# convert the object into a dict
kubernetes_recover_files_original_target_config_dict = kubernetes_recover_files_original_target_config_instance.to_dict()
# create an instance of KubernetesRecoverFilesOriginalTargetConfig from a dict
kubernetes_recover_files_original_target_config_from_dict = KubernetesRecoverFilesOriginalTargetConfig.from_dict(kubernetes_recover_files_original_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


