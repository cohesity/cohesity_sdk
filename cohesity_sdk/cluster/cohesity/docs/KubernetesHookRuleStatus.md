# KubernetesHookRuleStatus

This object represents the execution status of a quiesce/unquiesce rule that was applied during a backup run.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_quiescing_successful** | **bool, none_type** | Indicates whether the quiescing phase for this rule was successful. | [optional] 
**is_unquiescing_successful** | **bool, none_type** | Indicates whether the unquiescing phase for this rule was successful. | [optional] 
**pod_selector_labels** | **{str: (str,)}, none_type** | Key-value pairs representing the label selector used to match the pods for this rule. | [optional] 
**rule_index** | **int, none_type** | Index of the rule in the ordered list of rules applied during the run. | [optional] 
**uuid** | **str, none_type** | Universally unique identifier assigned to this rule. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


