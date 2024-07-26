# LifecycleRuleFilter

Specifies the filter used to identify objects that a Lifecycle Rule applies to. Note: All three properties are mutually exclusive.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_and** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the Lifecycle Rule Filter to apply a logical AND to two or more predicates. The Lifecycle Rule will apply to any object matching all of the predicates configured inside the AND operator. | [optional] 
**prefix** | **str, none_type** | Specifies the Prefix identifying one or more objects to which the rule applies. | [optional] 
**tag** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the tag in the object&#39;s tag set to which the rule applies. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


