# LifecycleRuleFilterAnd

Specifies the Lifecycle configuration Rule Filter AND element.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **str** | Specifies a Prefix identifying one or more objects to which the rule applies. | [optional] 
**tags** | [**List[LifecycleRuleFilterTag]**](LifecycleRuleFilterTag.md) | Specifies the tag in the object&#39;s tag set to which the rule applies. All of these tags must exist in the object&#39;s tag set in order for the rule to apply. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.lifecycle_rule_filter_and import LifecycleRuleFilterAnd

# TODO update the JSON string below
json = "{}"
# create an instance of LifecycleRuleFilterAnd from a JSON string
lifecycle_rule_filter_and_instance = LifecycleRuleFilterAnd.from_json(json)
# print the JSON string representation of the object
print(LifecycleRuleFilterAnd.to_json())

# convert the object into a dict
lifecycle_rule_filter_and_dict = lifecycle_rule_filter_and_instance.to_dict()
# create an instance of LifecycleRuleFilterAnd from a dict
lifecycle_rule_filter_and_from_dict = LifecycleRuleFilterAnd.from_dict(lifecycle_rule_filter_and_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


