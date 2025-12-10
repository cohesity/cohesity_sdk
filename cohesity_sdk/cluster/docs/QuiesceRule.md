# QuiesceRule

Specifies the Kubernetes Quiesce rule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pod_selector_labels** | [**List[KubernetesLabel]**](KubernetesLabel.md) | Specifies the labels to select a pod. | [optional] 
**post_snapshot_hooks** | [**List[KubernetesHook]**](KubernetesHook.md) | Specifies the hooks to be applied after taking snapshot. | 
**pre_snapshot_hooks** | [**List[KubernetesHook]**](KubernetesHook.md) | Specifies the hooks to be applied before taking snapshot. | 

## Example

```python
from cohesity_sdk.cluster.models.quiesce_rule import QuiesceRule

# TODO update the JSON string below
json = "{}"
# create an instance of QuiesceRule from a JSON string
quiesce_rule_instance = QuiesceRule.from_json(json)
# print the JSON string representation of the object
print(QuiesceRule.to_json())

# convert the object into a dict
quiesce_rule_dict = quiesce_rule_instance.to_dict()
# create an instance of QuiesceRule from a dict
quiesce_rule_from_dict = QuiesceRule.from_dict(quiesce_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


