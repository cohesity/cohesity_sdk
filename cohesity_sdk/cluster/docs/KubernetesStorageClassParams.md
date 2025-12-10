# KubernetesStorageClassParams

Specifies the storage class parameters for recovery of namespace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_class_mapping** | [**List[KubernetesLabel]**](KubernetesLabel.md) | Specifies mapping of storage classes | [optional] 
**use_storage_class_mapping** | **bool** | Specifies whether or not to use storage class mapping. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.kubernetes_storage_class_params import KubernetesStorageClassParams

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesStorageClassParams from a JSON string
kubernetes_storage_class_params_instance = KubernetesStorageClassParams.from_json(json)
# print the JSON string representation of the object
print(KubernetesStorageClassParams.to_json())

# convert the object into a dict
kubernetes_storage_class_params_dict = kubernetes_storage_class_params_instance.to_dict()
# create an instance of KubernetesStorageClassParams from a dict
kubernetes_storage_class_params_from_dict = KubernetesStorageClassParams.from_dict(kubernetes_storage_class_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


