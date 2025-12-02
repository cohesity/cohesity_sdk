# KubernetesProtectionGroupObjectParams

Specifies the object parameters to create Kubernetes Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_only_pvc** | **bool** | Specifies whether to backup pvc and related resources only | [optional] 
**exclude_object_ids** | **List[int]** | Specifies the object ids to be excluded for protection. This is supported for object protection on helios only | [optional] 
**exclude_params** | [**KubernetesFilterParams**](KubernetesFilterParams.md) |  | [optional] 
**exclude_pvcs** | [**List[KubernetesPvcInfo]**](KubernetesPvcInfo.md) | Specifies a list of pvcs to exclude from being protected. This is only applicable to kubernetes. | [optional] 
**excluded_resources** | **List[str]** | Specifies the resources to exclude during backup | [optional] 
**fail_backup_on_hook_failure** | **bool** | If true, fail backups when quiesce hook executions fail. | [optional] 
**id** | **int** | Specifies the id of the object. | 
**include_params** | [**KubernetesFilterParams**](KubernetesFilterParams.md) |  | [optional] 
**include_pvcs** | [**List[KubernetesPvcInfo]**](KubernetesPvcInfo.md) | Specifies a list of Pvcs to include in the protection. This is only applicable to kubernetes. | [optional] 
**included_resources** | **List[str]** | Specifies the resources to include during backup | [optional] 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 
**quiesce_groups** | [**List[QuiesceGroup]**](QuiesceGroup.md) | Specifies the quiescing rules are which specified by the user for doing backup. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.kubernetes_protection_group_object_params import KubernetesProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesProtectionGroupObjectParams from a JSON string
kubernetes_protection_group_object_params_instance = KubernetesProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(KubernetesProtectionGroupObjectParams.to_json())

# convert the object into a dict
kubernetes_protection_group_object_params_dict = kubernetes_protection_group_object_params_instance.to_dict()
# create an instance of KubernetesProtectionGroupObjectParams from a dict
kubernetes_protection_group_object_params_from_dict = KubernetesProtectionGroupObjectParams.from_dict(kubernetes_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


