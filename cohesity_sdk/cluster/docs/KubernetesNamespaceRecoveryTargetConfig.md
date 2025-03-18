# KubernetesNamespaceRecoveryTargetConfig

Specifies the recovery target configuration of the Namespace recovery.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**KubernetesNamespaceRecoveryNewSourceConfig**](KubernetesNamespaceRecoveryNewSourceConfig.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies whether or not to recover the Namespaces to a different source than they were backed up from. | 

## Example

```python
from cohesity_sdk.cluster.models.kubernetes_namespace_recovery_target_config import KubernetesNamespaceRecoveryTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesNamespaceRecoveryTargetConfig from a JSON string
kubernetes_namespace_recovery_target_config_instance = KubernetesNamespaceRecoveryTargetConfig.from_json(json)
# print the JSON string representation of the object
print(KubernetesNamespaceRecoveryTargetConfig.to_json())

# convert the object into a dict
kubernetes_namespace_recovery_target_config_dict = kubernetes_namespace_recovery_target_config_instance.to_dict()
# create an instance of KubernetesNamespaceRecoveryTargetConfig from a dict
kubernetes_namespace_recovery_target_config_from_dict = KubernetesNamespaceRecoveryTargetConfig.from_dict(kubernetes_namespace_recovery_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


