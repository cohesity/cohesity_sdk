# KubernetesLabel

Represents a single Kubernetes label.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the label, used to identify the label. | [optional] [readonly] 
**value** | **str** | The value associated with the label key. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.kubernetes_label import KubernetesLabel

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesLabel from a JSON string
kubernetes_label_instance = KubernetesLabel.from_json(json)
# print the JSON string representation of the object
print(KubernetesLabel.to_json())

# convert the object into a dict
kubernetes_label_dict = kubernetes_label_instance.to_dict()
# create an instance of KubernetesLabel from a dict
kubernetes_label_from_dict = KubernetesLabel.from_dict(kubernetes_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


