# KubernetesProtectionGroupObjectParams

Specifies the object parameters to create Kubernetes Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_pvcs** | [**List[KubernetesPvcInfo]**](KubernetesPvcInfo.md) | Specifies a list of pvcs to exclude from being protected. This is only applicable to kubernetes. | [optional] 
**id** | **int** | Specifies the id of the object. | 
**include_pvcs** | [**List[KubernetesPvcInfo]**](KubernetesPvcInfo.md) | Specifies a list of Pvcs to include in the protection. This is only applicable to kubernetes. | [optional] 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.kubernetes_protection_group_object_params import KubernetesProtectionGroupObjectParams

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


