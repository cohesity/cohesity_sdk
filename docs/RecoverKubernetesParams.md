# RecoverKubernetesParams

Specifies the recovery options specific to Kubernetes environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_namespace_params** | [**RecoverKubernetesNamespaceParams**](RecoverKubernetesNamespaceParams.md) |  | [optional] 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_kubernetes_params import RecoverKubernetesParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverKubernetesParams from a JSON string
recover_kubernetes_params_instance = RecoverKubernetesParams.from_json(json)
# print the JSON string representation of the object
print(RecoverKubernetesParams.to_json())

# convert the object into a dict
recover_kubernetes_params_dict = recover_kubernetes_params_instance.to_dict()
# create an instance of RecoverKubernetesParams from a dict
recover_kubernetes_params_from_dict = RecoverKubernetesParams.from_dict(recover_kubernetes_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


