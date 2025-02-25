# KubernetesProtectionGroupObjectParams

Specifies the object parameters to create Kubernetes Protection Group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the object. | 
**exclude_pvcs** | [**[KubernetesPvcInfo], none_type**](KubernetesPvcInfo.md) | Specifies a list of pvcs to exclude from being protected. This is only applicable to kubernetes. | [optional] 
**include_pvcs** | [**[KubernetesPvcInfo], none_type**](KubernetesPvcInfo.md) | Specifies a list of Pvcs to include in the protection. This is only applicable to kubernetes. | [optional] 
**name** | **str, none_type** | Specifies the name of the object. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


