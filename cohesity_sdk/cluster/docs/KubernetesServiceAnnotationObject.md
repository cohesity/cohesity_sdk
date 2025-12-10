# KubernetesServiceAnnotationObject

Specifies the service annotation key value pair while registering kubernetes source

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Specifies the service annotation key value | [optional] 
**value** | **str** | Specifies the service annotation value | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.kubernetes_service_annotation_object import KubernetesServiceAnnotationObject

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesServiceAnnotationObject from a JSON string
kubernetes_service_annotation_object_instance = KubernetesServiceAnnotationObject.from_json(json)
# print the JSON string representation of the object
print(KubernetesServiceAnnotationObject.to_json())

# convert the object into a dict
kubernetes_service_annotation_object_dict = kubernetes_service_annotation_object_instance.to_dict()
# create an instance of KubernetesServiceAnnotationObject from a dict
kubernetes_service_annotation_object_from_dict = KubernetesServiceAnnotationObject.from_dict(kubernetes_service_annotation_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


