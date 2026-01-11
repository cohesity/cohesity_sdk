# KubernetesTargetParamsForRecoverKubernetesNamespace

Specifies the parameters for recovering a Kubernetes namespace to a Kubernetes source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recovery_target_config** | [**KubernetesNamespaceRecoveryTargetConfig**](KubernetesNamespaceRecoveryTargetConfig.md) |  | 
**exclude_params** | [**KubernetesFilterParams**](KubernetesFilterParams.md) |  | [optional] 
**excluded_pvcs** | [**[KubernetesPvcInfo], none_type**](KubernetesPvcInfo.md) | Specifies the list of pvc to be excluded from recovery. This will be deprecated in the future. This is overridden by the object level param. | [optional] 
**include_params** | [**KubernetesFilterParams**](KubernetesFilterParams.md) |  | [optional] 
**objects** | [**[KubernetesRecoveryObjectParams], none_type**](CommonRecoverObjectSnapshotParams.md) | Specifies the objects to be recovered. | [optional] 
**preserve_mac_address** | **bool, none_type** | Specifies whether to preserve mac address for restored vm. Default is false. | [optional] 
**recover_cluster_scoped_resources** | [**RecoverClusterScopedResourcesParams**](RecoverClusterScopedResourcesParams.md) |  | [optional] 
**recover_protection_group_runs_params** | [**[RecoverProtectionGroupRunParams], none_type**](RecoverProtectionGroupRunParams.md) | Specifies the Protection Group Runs params to recover. All the VM&#39;s that are successfully backed up by specified Runs will be recovered. This can be specified along with individual snapshots of VMs. User has to make sure that specified Object snapshots and Protection Group Runs should not have any intersection. For example, user cannot specify multiple Runs which has same Object or an Object snapshot and a Run which has same Object&#39;s snapshot. | [optional] 
**recover_pvcs_only** | **bool, none_type** | Specifies whether to recover PVCs only during recovery. This is overridden with the object level settings and will be deprecated in the future. | [optional] 
**recovery_region_migration_params** | [**KubernetesRecoveryMigrationParams**](KubernetesRecoveryMigrationParams.md) |  | [optional] 
**recovery_zone_migration_params** | [**[KubernetesRecoveryMigrationParams], none_type**](KubernetesRecoveryMigrationParams.md) | Specifies rules for performing zone migrations during recovery. Used in case of recovery to new location and the namespace being recovered is in a different zone. | [optional] 
**rename_recovered_namespaces_params** | [**RecoveredOrClonedVmsRenameConfig**](RecoveredOrClonedVmsRenameConfig.md) |  | [optional] 
**skip_cluster_compatibility_check** | **bool, none_type** | Specifies whether to skip checking if the target cluster, to restore to, is compatible or not. By default restore allowed to compatible cluster only | [optional] 
**storage_class** | [**KubernetesStorageClassParams**](KubernetesStorageClassParams.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


