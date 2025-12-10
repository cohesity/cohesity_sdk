# KubernetesRecoverFilesNewTargetConfig

Specifies the configuration for recovering files and folders to a new target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**absolute_path** | **str** | Specifies the absolute path of the file. | 
**target_namespace** | [**RecoverTarget**](RecoverTarget.md) |  | [optional] 
**target_pvc** | [**RecoverTarget**](RecoverTarget.md) |  | 
**target_source** | [**RecoverTarget**](RecoverTarget.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.kubernetes_recover_files_new_target_config import KubernetesRecoverFilesNewTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesRecoverFilesNewTargetConfig from a JSON string
kubernetes_recover_files_new_target_config_instance = KubernetesRecoverFilesNewTargetConfig.from_json(json)
# print the JSON string representation of the object
print(KubernetesRecoverFilesNewTargetConfig.to_json())

# convert the object into a dict
kubernetes_recover_files_new_target_config_dict = kubernetes_recover_files_new_target_config_instance.to_dict()
# create an instance of KubernetesRecoverFilesNewTargetConfig from a dict
kubernetes_recover_files_new_target_config_from_dict = KubernetesRecoverFilesNewTargetConfig.from_dict(kubernetes_recover_files_new_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


