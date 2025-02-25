# KubernetesTargetParamsForRecoverKubernetesNamespace

Specifies the parameters for recovering a Kubernetes namespace to a Kubernetes source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recovery_target_config** | [**KubernetesNamespaceRecoveryTargetConfig**](KubernetesNamespaceRecoveryTargetConfig.md) |  | 
**excluded_pvcs** | [**[KubernetesPvcInfo], none_type**](KubernetesPvcInfo.md) | Specifies the list of pvc to be excluded from recovery. | [optional] 
**objects** | [**[CommonRecoverObjectSnapshotParams], none_type**](CommonRecoverObjectSnapshotParams.md) | Specifies the objects to be recovered. | [optional] 
**recover_protection_group_runs_params** | [**[RecoverProtectionGroupRunParams], none_type**](RecoverProtectionGroupRunParams.md) | Specifies the Protection Group Runs params to recover. All the VM&#39;s that are successfully backed up by specified Runs will be recovered. This can be specified along with individual snapshots of VMs. User has to make sure that specified Object snapshots and Protection Group Runs should not have any intersection. For example, user cannot specify multiple Runs which has same Object or an Object snapshot and a Run which has same Object&#39;s snapshot. | [optional] 
**rename_recovered_namespaces_params** | [**RecoveredOrClonedVmsRenameConfig**](RecoveredOrClonedVmsRenameConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


