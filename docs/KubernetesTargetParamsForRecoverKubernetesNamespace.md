# KubernetesTargetParamsForRecoverKubernetesNamespace

Specifies the parameters for recovering a Kubernetes namespace to a Kubernetes source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excluded_pvcs** | [**List[KubernetesPvcInfo]**](KubernetesPvcInfo.md) | Specifies the list of pvc to be excluded from recovery. | [optional] 
**objects** | [**List[CommonRecoverObjectSnapshotParams]**](CommonRecoverObjectSnapshotParams.md) | Specifies the objects to be recovered. | [optional] 
**recover_protection_group_runs_params** | [**List[RecoverProtectionGroupRunParams]**](RecoverProtectionGroupRunParams.md) | Specifies the Protection Group Runs params to recover. All the VM&#39;s that are successfully backed up by specified Runs will be recovered. This can be specified along with individual snapshots of VMs. User has to make sure that specified Object snapshots and Protection Group Runs should not have any intersection. For example, user cannot specify multiple Runs which has same Object or an Object snapshot and a Run which has same Object&#39;s snapshot. | [optional] 
**recovery_target_config** | [**KubernetesNamespaceRecoveryTargetConfig**](KubernetesNamespaceRecoveryTargetConfig.md) |  | 
**rename_recovered_namespaces_params** | [**RecoveredOrClonedVmsRenameConfig**](RecoveredOrClonedVmsRenameConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.kubernetes_target_params_for_recover_kubernetes_namespace import KubernetesTargetParamsForRecoverKubernetesNamespace

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesTargetParamsForRecoverKubernetesNamespace from a JSON string
kubernetes_target_params_for_recover_kubernetes_namespace_instance = KubernetesTargetParamsForRecoverKubernetesNamespace.from_json(json)
# print the JSON string representation of the object
print(KubernetesTargetParamsForRecoverKubernetesNamespace.to_json())

# convert the object into a dict
kubernetes_target_params_for_recover_kubernetes_namespace_dict = kubernetes_target_params_for_recover_kubernetes_namespace_instance.to_dict()
# create an instance of KubernetesTargetParamsForRecoverKubernetesNamespace from a dict
kubernetes_target_params_for_recover_kubernetes_namespace_from_dict = KubernetesTargetParamsForRecoverKubernetesNamespace.from_dict(kubernetes_target_params_for_recover_kubernetes_namespace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


