# KubernetesNamespaceRecoveryNewSourceConfig

Specifies the new source configuration if a Kubernetes Namespace is being restored to a different source than the one from which it was protected.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.models.kubernetes_namespace_recovery_new_source_config import KubernetesNamespaceRecoveryNewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesNamespaceRecoveryNewSourceConfig from a JSON string
kubernetes_namespace_recovery_new_source_config_instance = KubernetesNamespaceRecoveryNewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(KubernetesNamespaceRecoveryNewSourceConfig.to_json())

# convert the object into a dict
kubernetes_namespace_recovery_new_source_config_dict = kubernetes_namespace_recovery_new_source_config_instance.to_dict()
# create an instance of KubernetesNamespaceRecoveryNewSourceConfig from a dict
kubernetes_namespace_recovery_new_source_config_from_dict = KubernetesNamespaceRecoveryNewSourceConfig.from_dict(kubernetes_namespace_recovery_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


