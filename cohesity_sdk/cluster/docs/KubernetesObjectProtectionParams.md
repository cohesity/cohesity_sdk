# KubernetesObjectProtectionParams

Specifies the parameters that are specific to Kubernetes Object Protection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[KubernetesProtectionGroupObjectParams]**](KubernetesProtectionGroupObjectParams.md) | Specifies the objects to be included in Protection. | 
**enable_indexing** | **bool, none_type** | Specifies if indexing of files and folders is allowed or not while backing up namespace. If allowed files and folder can be recovered. Default: False | [optional] 
**exclude_label_ids** | **[[int]]** | Array of arrays of label IDs that specify labels to exclude. Optionally specify a list of labels to exclude from protecting by listing protection source ids of labels in this two dimensional array. Using this two dimensional array of label IDs, the Cluster generates a list of namespaces to exclude from protecting, which are derived from intersections of the inner arrays and union of the outer array. This is not supported for object protection on helios. | [optional] 
**exclude_object_ids** | **[int]** | Specifies the object ids to be excluded for protection. This is not supported for object protection on helios. | [optional] 
**exclude_params** | [**KubernetesFilterParams**](KubernetesFilterParams.md) |  | [optional] 
**include_params** | [**KubernetesFilterParams**](KubernetesFilterParams.md) |  | [optional] 
**label_ids** | **[[int]], none_type** | Array of array of label IDs that specify labels to protect. Optionally specify a list of labels to protect by listing protection source ids of labels in this two dimensional array. Using this two dimensional array of label IDs, the cluster generates a list of namespaces to protect, which are derived from intersections of the inner arrays and union of the outer array. This is not supported for object protection on helios. | [optional] 
**leverage_csi_snapshot** | **bool, none_type** | Specifies if CSI snapshots should be used for backup of namespaces. Default: False | [optional] 
**non_snapshot_backup** | **bool, none_type** | Specifies whether to fallback to a non-snapshot backup for PVC in case the snapshot backup fails. Default: False | [optional] 
**volume_backup_failure** | **bool, none_type** | Specifies whether to ignore the failure of a volume while backing up and proceed with the backup. Default: False | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


