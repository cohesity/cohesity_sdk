# KubernetesTargetParamsForRecoverKubernetesNamespace

Specifies the parameters for recovering a Kubernetes namespace to a Kubernetes source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_params** | [**KubernetesFilterParams**](KubernetesFilterParams.md) |  | [optional] 
**excluded_pvcs** | [**List[KubernetesPvcInfo]**](KubernetesPvcInfo.md) | Specifies the list of pvc to be excluded from recovery. This will be deprecated in the future. This is overridden by the object level param. | [optional] 
**include_params** | [**KubernetesFilterParams**](KubernetesFilterParams.md) |  | [optional] 
**objects** | [**List[CommonRecoverObjectSnapshotParams]**](CommonRecoverObjectSnapshotParams.md) | Specifies the objects to be recovered. | [optional] 
**preserve_mac_address** | **bool** | Specifies whether to preserve mac address for restored vm. Default is false. | [optional] 
**recover_cluster_scoped_resources** | [**RecoverClusterScopedResourcesParams**](RecoverClusterScopedResourcesParams.md) |  | [optional] 
**recover_protection_group_runs_params** | [**List[RecoverProtectionGroupRunParams]**](RecoverProtectionGroupRunParams.md) | Specifies the Protection Group Runs params to recover. All the VM&#39;s that are successfully backed up by specified Runs will be recovered. This can be specified along with individual snapshots of VMs. User has to make sure that specified Object snapshots and Protection Group Runs should not have any intersection. For example, user cannot specify multiple Runs which has same Object or an Object snapshot and a Run which has same Object&#39;s snapshot. | [optional] 
**recover_pvcs_only** | **bool** | Specifies whether to recover PVCs only during recovery. This is overridden with the object level settings and will be deprecated in the future. | [optional] 
**recovery_region_migration_params** | [**KubernetesRecoveryMigrationParams**](KubernetesRecoveryMigrationParams.md) |  | [optional] 
**recovery_target_config** | [**KubernetesNamespaceRecoveryTargetConfig**](KubernetesNamespaceRecoveryTargetConfig.md) |  | 
**recovery_zone_migration_params** | [**List[KubernetesRecoveryMigrationParams]**](KubernetesRecoveryMigrationParams.md) | Specifies rules for performing zone migrations during recovery. Used in case of recovery to new location and the namespace being recovered is in a different zone. | [optional] 
**rename_recovered_namespaces_params** | [**RecoveredOrClonedVmsRenameConfig**](RecoveredOrClonedVmsRenameConfig.md) |  | [optional] 
**skip_cluster_compatibility_check** | **bool** | Specifies whether to skip checking if the target cluster, to restore to, is compatible or not. By default restore allowed to compatible cluster only | [optional] 
**storage_class** | [**KubernetesStorageClassParams**](KubernetesStorageClassParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.kubernetes_target_params_for_recover_kubernetes_namespace import KubernetesTargetParamsForRecoverKubernetesNamespace

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


