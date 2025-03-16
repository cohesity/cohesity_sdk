# RecoverKubernetesNamespaceParams

Specifies the parameters to recover Kubernetes Namespaces.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kubernetes_target_params** | [**KubernetesTargetParamsForRecoverKubernetesNamespace**](KubernetesTargetParamsForRecoverKubernetesNamespace.md) | Specifies the params for recovering to a Kubernetes host. | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) | Specifies VLAN Params associated with the recovered. If this is not specified, then the VLAN settings will be automatically selected from one of the below options: a. If VLANs are configured on Cohesity, then the VLAN host/VIP will be automatically based on the client&#39;s (e.g. ESXI host) IP address. b. If VLANs are not configured on Cohesity, then the partition hostname or VIPs will be used for Recovery. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.recover_kubernetes_namespace_params import RecoverKubernetesNamespaceParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverKubernetesNamespaceParams from a JSON string
recover_kubernetes_namespace_params_instance = RecoverKubernetesNamespaceParams.from_json(json)
# print the JSON string representation of the object
print(RecoverKubernetesNamespaceParams.to_json())

# convert the object into a dict
recover_kubernetes_namespace_params_dict = recover_kubernetes_namespace_params_instance.to_dict()
# create an instance of RecoverKubernetesNamespaceParams from a dict
recover_kubernetes_namespace_params_from_dict = RecoverKubernetesNamespaceParams.from_dict(recover_kubernetes_namespace_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


