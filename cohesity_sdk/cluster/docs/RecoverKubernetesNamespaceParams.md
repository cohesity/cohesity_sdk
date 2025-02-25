# RecoverKubernetesNamespaceParams

Specifies the parameters to recover Kubernetes Namespaces.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | defaults to "kKubernetes"
**kubernetes_target_params** | [**KubernetesTargetParamsForRecoverKubernetesNamespace**](KubernetesTargetParamsForRecoverKubernetesNamespace.md) |  | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


