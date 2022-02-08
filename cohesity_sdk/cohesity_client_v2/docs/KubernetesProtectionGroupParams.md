# KubernetesProtectionGroupParams

Specifies the parameters which are related to Kubernetes Protection Groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[KubernetesProtectionGroupObjectParams]**](KubernetesProtectionGroupObjectParams.md) | Specifies the objects included in the Protection Group. | [optional] 
**exclude_object_ids** | **[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**source_id** | **int, none_type** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str, none_type** | Specifies the name of the parent of the objects. | [optional] [readonly] 
**label_ids** | **[[int]], none_type** | Array of array of label IDs that specify labels to protect. Optionally specify a list of labels to protect by listing protection source ids of labels in this two dimensional array. Using this two dimensional array of label IDs, the cluster generates a list of namespaces to protect, which are derived from intersections of the inner arrays and union of the outer array. | [optional] 
**exclude_label_ids** | **[[int]]** | Array of arrays of label IDs that specify labels to exclude. Optionally specify a list of labels to exclude from protecting by listing protection source ids of labels in this two dimensional array. Using this two dimensional array of label IDs, the Cluster generates a list of namespaces to exclude from protecting, which are derived from intersections of the inner arrays and union of the outer array. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


