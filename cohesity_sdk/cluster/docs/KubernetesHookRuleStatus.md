# KubernetesHookRuleStatus

This object represents the execution status of a quiesce/unquiesce rule that was applied during a backup run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_quiescing_successful** | **bool** | Indicates whether the quiescing phase for this rule was successful. | [optional] 
**is_unquiescing_successful** | **bool** | Indicates whether the unquiescing phase for this rule was successful. | [optional] 
**pod_selector_labels** | **Dict[str, str]** | Key-value pairs representing the label selector used to match the pods for this rule. | [optional] 
**rule_index** | **int** | Index of the rule in the ordered list of rules applied during the run. | [optional] 
**uuid** | **str** | Universally unique identifier assigned to this rule. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.kubernetes_hook_rule_status import KubernetesHookRuleStatus

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesHookRuleStatus from a JSON string
kubernetes_hook_rule_status_instance = KubernetesHookRuleStatus.from_json(json)
# print the JSON string representation of the object
print(KubernetesHookRuleStatus.to_json())

# convert the object into a dict
kubernetes_hook_rule_status_dict = kubernetes_hook_rule_status_instance.to_dict()
# create an instance of KubernetesHookRuleStatus from a dict
kubernetes_hook_rule_status_from_dict = KubernetesHookRuleStatus.from_dict(kubernetes_hook_rule_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


