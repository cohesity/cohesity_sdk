# ConstructMetaInfoKubernetesParams

Params to fetch resource info for a kubernetes object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_id** | **int** | Specifies the type of object id to fetch resources | 

## Example

```python
from cohesity_sdk.cluster.models.construct_meta_info_kubernetes_params import ConstructMetaInfoKubernetesParams

# TODO update the JSON string below
json = "{}"
# create an instance of ConstructMetaInfoKubernetesParams from a JSON string
construct_meta_info_kubernetes_params_instance = ConstructMetaInfoKubernetesParams.from_json(json)
# print the JSON string representation of the object
print(ConstructMetaInfoKubernetesParams.to_json())

# convert the object into a dict
construct_meta_info_kubernetes_params_dict = construct_meta_info_kubernetes_params_instance.to_dict()
# create an instance of ConstructMetaInfoKubernetesParams from a dict
construct_meta_info_kubernetes_params_from_dict = ConstructMetaInfoKubernetesParams.from_dict(construct_meta_info_kubernetes_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


