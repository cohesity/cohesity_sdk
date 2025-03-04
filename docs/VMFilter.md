# VMFilter

Specifies the VM filter details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_string** | **str** | Specifies the filter string using wildcard supported strings or regular expressions. | [optional] 
**is_regular_expression** | **bool** | Specifies whether the provided filter string is a regular expression or not. This needs to be explicitly set to true if user is trying to filter by regular expressions. Not providing this value in case of regular expression can result in unintended results. The default value is assumed to be false. | [optional] [default to False]
**case_sensitive** | **bool** | Specifies whether the provided filter string is case sensitive or not. This needs to be explicitly set to true if user is trying to filter by case sensitive expressions. The default value is assumed to be false. | [optional] [default to False]

## Example

```python
from cohesity_sdk.models.vm_filter import VMFilter

# TODO update the JSON string below
json = "{}"
# create an instance of VMFilter from a JSON string
vm_filter_instance = VMFilter.from_json(json)
# print the JSON string representation of the object
print(VMFilter.to_json())

# convert the object into a dict
vm_filter_dict = vm_filter_instance.to_dict()
# create an instance of VMFilter from a dict
vm_filter_from_dict = VMFilter.from_dict(vm_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


