# KubernetesProtectionGroupParams

Specifies the parameters which are related to Kubernetes Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_label_ids** | **List[List[int]]** | Array of arrays of label IDs that specify labels to exclude. Optionally specify a list of labels to exclude from protecting by listing protection source ids of labels in this two dimensional array. Using this two dimensional array of label IDs, the Cluster generates a list of namespaces to exclude from protecting, which are derived from intersections of the inner arrays and union of the outer array. | [optional] 
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**exclude_params** | [**KubernetesFilterParams**](KubernetesFilterParams.md) |  | [optional] 
**include_params** | [**KubernetesFilterParams**](KubernetesFilterParams.md) |  | [optional] 
**label_ids** | **List[List[int]]** | Array of array of label IDs that specify labels to protect. Optionally specify a list of labels to protect by listing protection source ids of labels in this two dimensional array. Using this two dimensional array of label IDs, the cluster generates a list of namespaces to protect, which are derived from intersections of the inner arrays and union of the outer array. | [optional] 
**leverage_csi_snapshot** | **bool** | Specifies if CSI snapshots should be used for backup of namespaces. | [optional] 
**objects** | [**List[KubernetesProtectionGroupObjectParams]**](KubernetesProtectionGroupObjectParams.md) | Specifies the objects included in the Protection Group. | [optional] 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 
**vlan_params** | [**VlanParams**](VlanParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.kubernetes_protection_group_params import KubernetesProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesProtectionGroupParams from a JSON string
kubernetes_protection_group_params_instance = KubernetesProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(KubernetesProtectionGroupParams.to_json())

# convert the object into a dict
kubernetes_protection_group_params_dict = kubernetes_protection_group_params_instance.to_dict()
# create an instance of KubernetesProtectionGroupParams from a dict
kubernetes_protection_group_params_from_dict = KubernetesProtectionGroupParams.from_dict(kubernetes_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


