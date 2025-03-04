# Filter

Specifies the filter details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_string** | **str** | Specifies the filter string using wildcard supported strings or regular expressions. | [optional] 
**is_regular_expression** | **bool** | Specifies whether the provided filter string is a regular expression or not. This needs to be explicitly set to true if user is trying to filter by regular expressions. Not providing this value in case of regular expression can result in unintended results. The default value is assumed to be false. | [optional] [default to False]

## Example

```python
from cohesity_sdk.models.filter import Filter

# TODO update the JSON string below
json = "{}"
# create an instance of Filter from a JSON string
filter_instance = Filter.from_json(json)
# print the JSON string representation of the object
print(Filter.to_json())

# convert the object into a dict
filter_dict = filter_instance.to_dict()
# create an instance of Filter from a dict
filter_from_dict = Filter.from_dict(filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


