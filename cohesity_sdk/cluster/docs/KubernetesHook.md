# KubernetesHook

Specifies the set of parameters for applying scripts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commands** | **List[str]** | Specifies the commands. | 
**container** | **str** | Specifies the name of the container. | [optional] 
**fail_on_error** | **bool** | Specifies whether to fail on error or not. | [optional] 
**timeout** | **int** | Specifies timeout for the operation. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.kubernetes_hook import KubernetesHook

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesHook from a JSON string
kubernetes_hook_instance = KubernetesHook.from_json(json)
# print the JSON string representation of the object
print(KubernetesHook.to_json())

# convert the object into a dict
kubernetes_hook_dict = kubernetes_hook_instance.to_dict()
# create an instance of KubernetesHook from a dict
kubernetes_hook_from_dict = KubernetesHook.from_dict(kubernetes_hook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


