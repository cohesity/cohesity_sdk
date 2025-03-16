# LifecycleRuleFilterTag

Specifies the Lifecycle configuration Rule Filter Tag element.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Specifies the Name of the object key. | [optional] 
**value** | **str** | Specifies the Value of the tag. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.lifecycle_rule_filter_tag import LifecycleRuleFilterTag

# TODO update the JSON string below
json = "{}"
# create an instance of LifecycleRuleFilterTag from a JSON string
lifecycle_rule_filter_tag_instance = LifecycleRuleFilterTag.from_json(json)
# print the JSON string representation of the object
print(LifecycleRuleFilterTag.to_json())

# convert the object into a dict
lifecycle_rule_filter_tag_dict = lifecycle_rule_filter_tag_instance.to_dict()
# create an instance of LifecycleRuleFilterTag from a dict
lifecycle_rule_filter_tag_from_dict = LifecycleRuleFilterTag.from_dict(lifecycle_rule_filter_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


