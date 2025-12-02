# KubernetesProtectionGroupObjectParams

Specifies the object parameters to create Kubernetes Protection Group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the object. | 
**backup_only_pvc** | **bool, none_type** | Specifies whether to backup pvc and related resources only | [optional] 
**exclude_object_ids** | **[int], none_type** | Specifies the object ids to be excluded for protection. This is supported for object protection on helios only | [optional] 
**exclude_params** | [**KubernetesFilterParams**](KubernetesFilterParams.md) |  | [optional] 
**exclude_pvcs** | [**[KubernetesPvcInfo], none_type**](KubernetesPvcInfo.md) | Specifies a list of pvcs to exclude from being protected. This is only applicable to kubernetes. | [optional] 
**excluded_resources** | **[str], none_type** | Specifies the resources to exclude during backup | [optional] 
**fail_backup_on_hook_failure** | **bool, none_type** | If true, fail backups when quiesce hook executions fail. | [optional] 
**include_params** | [**KubernetesFilterParams**](KubernetesFilterParams.md) |  | [optional] 
**include_pvcs** | [**[KubernetesPvcInfo], none_type**](KubernetesPvcInfo.md) | Specifies a list of Pvcs to include in the protection. This is only applicable to kubernetes. | [optional] 
**included_resources** | **[str], none_type** | Specifies the resources to include during backup | [optional] 
**name** | **str, none_type** | Specifies the name of the object. | [optional] [readonly] 
**quiesce_groups** | [**[QuiesceGroup], none_type**](QuiesceGroup.md) | Specifies the quiescing rules are which specified by the user for doing backup. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


