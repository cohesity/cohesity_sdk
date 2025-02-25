# FilerLifecycleRule

Specifies the Lifecycle configuration rule.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the Unique identifier for the rule. No 2 rules in a policy should have the same name. The value cannot be longer than 255 characters. | 
**status** | **str, none_type** | Specifies if the rule is currently being applied. | 
**type** | **str, none_type** | Specifies if the rule is Allow or Deny type. | 
**aging_policy** | [**FilerLifecycleAgingPolicy**](FilerLifecycleAgingPolicy.md) |  | [optional] 
**file_filter** | [**FilerLifecycleRuleFilter**](FilerLifecycleRuleFilter.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


