# KubernetesObjectProtectionParams

Specifies the parameters that are specific to Kubernetes Object Protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_indexing** | **bool** | Specifies if indexing of files and folders is allowed or not while backing up namespace. If allowed files and folder can be recovered. Default: False | [optional] 
**exclude_label_ids** | **List[List[int]]** | Array of arrays of label IDs that specify labels to exclude. Optionally specify a list of labels to exclude from protecting by listing protection source ids of labels in this two dimensional array. Using this two dimensional array of label IDs, the Cluster generates a list of namespaces to exclude from protecting, which are derived from intersections of the inner arrays and union of the outer array. This is not supported for object protection on helios. | [optional] 
**exclude_object_ids** | **List[int]** | Specifies the object ids to be excluded for protection. This is not supported for object protection on helios. | [optional] 
**exclude_params** | [**KubernetesFilterParams**](KubernetesFilterParams.md) |  | [optional] 
**include_params** | [**KubernetesFilterParams**](KubernetesFilterParams.md) |  | [optional] 
**label_ids** | **List[List[int]]** | Array of array of label IDs that specify labels to protect. Optionally specify a list of labels to protect by listing protection source ids of labels in this two dimensional array. Using this two dimensional array of label IDs, the cluster generates a list of namespaces to protect, which are derived from intersections of the inner arrays and union of the outer array. This is not supported for object protection on helios. | [optional] 
**leverage_csi_snapshot** | **bool** | Specifies if CSI snapshots should be used for backup of namespaces. Default: False | [optional] 
**non_snapshot_backup** | **bool** | Specifies whether to fallback to a non-snapshot backup for PVC in case the snapshot backup fails. Default: False | [optional] 
**objects** | [**List[KubernetesProtectionGroupObjectParams]**](KubernetesProtectionGroupObjectParams.md) | Specifies the objects to be included in Protection. | 
**volume_backup_failure** | **bool** | Specifies whether to ignore the failure of a volume while backing up and proceed with the backup. Default: False | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.kubernetes_object_protection_params import KubernetesObjectProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesObjectProtectionParams from a JSON string
kubernetes_object_protection_params_instance = KubernetesObjectProtectionParams.from_json(json)
# print the JSON string representation of the object
print(KubernetesObjectProtectionParams.to_json())

# convert the object into a dict
kubernetes_object_protection_params_dict = kubernetes_object_protection_params_instance.to_dict()
# create an instance of KubernetesObjectProtectionParams from a dict
kubernetes_object_protection_params_from_dict = KubernetesObjectProtectionParams.from_dict(kubernetes_object_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


