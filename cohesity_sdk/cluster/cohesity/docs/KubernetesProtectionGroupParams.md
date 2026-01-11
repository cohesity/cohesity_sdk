# KubernetesProtectionGroupParams

Specifies the parameters which are related to Kubernetes Protection Groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_indexing** | **bool, none_type** | Specifies if indexing of files and folders is allowed or not while backing up namespace. If allowed files and folder can be recovered. | [optional] 
**exclude_label_ids** | **[[int]]** | Array of arrays of label IDs that specify labels to exclude. Optionally specify a list of labels to exclude from protecting by listing protection source ids of labels in this two dimensional array. Using this two dimensional array of label IDs, the Cluster generates a list of namespaces to exclude from protecting, which are derived from intersections of the inner arrays and union of the outer array. | [optional] 
**exclude_object_ids** | **[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**exclude_params** | [**KubernetesFilterParams**](KubernetesFilterParams.md) |  | [optional] 
**include_params** | [**KubernetesFilterParams**](KubernetesFilterParams.md) |  | [optional] 
**label_ids** | **[[int]], none_type** | Array of array of label IDs that specify labels to protect. Optionally specify a list of labels to protect by listing protection source ids of labels in this two dimensional array. Using this two dimensional array of label IDs, the cluster generates a list of namespaces to protect, which are derived from intersections of the inner arrays and union of the outer array. | [optional] 
**leverage_csi_snapshot** | **bool, none_type** | Specifies if CSI snapshots should be used for backup of namespaces. | [optional] 
**non_snapshot_backup** | **bool, none_type** | Specifies if snapshot backup fails, non-snapshot backup will be proceeded. | [optional] 
**objects** | [**[KubernetesProtectionGroupObjectParams]**](KubernetesProtectionGroupObjectParams.md) | Specifies the objects included in the Protection Group. | [optional] 
**perform_source_side_deduplication** | **bool, none_type** | Specifies whether or not to perform source side deduplication on this Protection Group. | [optional] 
**source_id** | **int, none_type** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str, none_type** | Specifies the name of the parent of the objects. | [optional] [readonly] 
**vlan_params** | [**VlanParams**](VlanParams.md) |  | [optional] 
**volume_backup_failure** | **bool, none_type** | Specifies whether to process with backup if volumes backup fails. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


