# GetViewTemplatesResult

Specifies the list of view template returned that matched the specified filter criteria.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**templates** | [**List[Template]**](Template.md) | Array of view template. Specifies the list of view templates returned in this response. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.get_view_templates_result import GetViewTemplatesResult

# TODO update the JSON string below
json = "{}"
# create an instance of GetViewTemplatesResult from a JSON string
get_view_templates_result_instance = GetViewTemplatesResult.from_json(json)
# print the JSON string representation of the object
print(GetViewTemplatesResult.to_json())

# convert the object into a dict
get_view_templates_result_dict = get_view_templates_result_instance.to_dict()
# create an instance of GetViewTemplatesResult from a dict
get_view_templates_result_from_dict = GetViewTemplatesResult.from_dict(get_view_templates_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


