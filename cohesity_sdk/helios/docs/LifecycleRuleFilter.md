# LifecycleRuleFilter

Specifies the filter used to identify objects that a Lifecycle Rule applies to. Note: All three properties are mutually exclusive.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**LifecycleRuleFilterAnd**](LifecycleRuleFilterAnd.md) | Specifies the Lifecycle Rule Filter to apply a logical AND to two or more predicates. The Lifecycle Rule will apply to any object matching all of the predicates configured inside the AND operator. | [optional] 
**prefix** | **str** | Specifies the Prefix identifying one or more objects to which the rule applies. | [optional] 
**tag** | [**LifecycleRuleFilterTag**](LifecycleRuleFilterTag.md) | Specifies the tag in the object&#39;s tag set to which the rule applies. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.lifecycle_rule_filter import LifecycleRuleFilter

# TODO update the JSON string below
json = "{}"
# create an instance of LifecycleRuleFilter from a JSON string
lifecycle_rule_filter_instance = LifecycleRuleFilter.from_json(json)
# print the JSON string representation of the object
print(LifecycleRuleFilter.to_json())

# convert the object into a dict
lifecycle_rule_filter_dict = lifecycle_rule_filter_instance.to_dict()
# create an instance of LifecycleRuleFilter from a dict
lifecycle_rule_filter_from_dict = LifecycleRuleFilter.from_dict(lifecycle_rule_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


