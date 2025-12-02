# KubernetesLabelObject

Specifies the object containing key value pair for resource label and annotations to annotate cohesity deployed resources and services for a k8s source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Specifies the label key | 
**value** | **str** | Specifies the label value | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.kubernetes_label_object import KubernetesLabelObject

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesLabelObject from a JSON string
kubernetes_label_object_instance = KubernetesLabelObject.from_json(json)
# print the JSON string representation of the object
print(KubernetesLabelObject.to_json())

# convert the object into a dict
kubernetes_label_object_dict = kubernetes_label_object_instance.to_dict()
# create an instance of KubernetesLabelObject from a dict
kubernetes_label_object_from_dict = KubernetesLabelObject.from_dict(kubernetes_label_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


