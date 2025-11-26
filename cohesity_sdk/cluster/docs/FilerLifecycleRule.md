# FilerLifecycleRule

Specifies the Lifecycle configuration rule.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the Unique identifier for the rule. No 2 rules in a policy should have the same name. The value cannot be longer than 255 characters. | 
**status** | **str, none_type** | Specifies if the rule is currently being applied. | 
**type** | **str, none_type** | Specifies if the rule is Allow or Deny type. | 
**aging_policy** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the file&#39;s selection based on of the following: last modification time, creation time or last access time. This filed is mandatory for rules that are Allow type. Note: Both the fields days and dateInUsecs are mutually exclusive to each other. | [optional] 
**file_filter** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the filter used to identify files that a Lifecycle Rule applies to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


