# FilerLifecycleRuleFilter

Specifies the filter used to identify files that a Lifecycle Rule applies to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_extensions** | **List[str]** | Specifies the file&#39;s selection based on their extension. Eg: .pdf, .txt, etc. Note: Provide extensions here with the initial &#39;.&#39; character, example .pdf and not pdf. Extensions are case-insensitive, i.e. .pdf extension in filter will delete all files have .pdf, .PDF, .pDF, etc. | [optional] 
**file_size** | [**FilerLifecycleSizeFilter**](FilerLifecycleSizeFilter.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.filer_lifecycle_rule_filter import FilerLifecycleRuleFilter

# TODO update the JSON string below
json = "{}"
# create an instance of FilerLifecycleRuleFilter from a JSON string
filer_lifecycle_rule_filter_instance = FilerLifecycleRuleFilter.from_json(json)
# print the JSON string representation of the object
print(FilerLifecycleRuleFilter.to_json())

# convert the object into a dict
filer_lifecycle_rule_filter_dict = filer_lifecycle_rule_filter_instance.to_dict()
# create an instance of FilerLifecycleRuleFilter from a dict
filer_lifecycle_rule_filter_from_dict = FilerLifecycleRuleFilter.from_dict(filer_lifecycle_rule_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


