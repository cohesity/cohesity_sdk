# FilerLifecycleRule

Specifies the Lifecycle configuration rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aging_policy** | [**FilerLifecycleAgingPolicy**](FilerLifecycleAgingPolicy.md) |  | [optional] 
**file_filter** | [**FilerLifecycleRuleFilter**](FilerLifecycleRuleFilter.md) |  | [optional] 
**name** | **str** | Specifies the Unique identifier for the rule. No 2 rules in a policy should have the same name. The value cannot be longer than 255 characters. | 
**status** | **str** | Specifies if the rule is currently being applied. | 
**type** | **str** | Specifies if the rule is Allow or Deny type. | 

## Example

```python
from cohesity_sdk.models.filer_lifecycle_rule import FilerLifecycleRule

# TODO update the JSON string below
json = "{}"
# create an instance of FilerLifecycleRule from a JSON string
filer_lifecycle_rule_instance = FilerLifecycleRule.from_json(json)
# print the JSON string representation of the object
print(FilerLifecycleRule.to_json())

# convert the object into a dict
filer_lifecycle_rule_dict = filer_lifecycle_rule_instance.to_dict()
# create an instance of FilerLifecycleRule from a dict
filer_lifecycle_rule_from_dict = FilerLifecycleRule.from_dict(filer_lifecycle_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


