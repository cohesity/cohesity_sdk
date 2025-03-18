# Template

Description of the view template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compress** | **bool** | Specifies whether to enable compression in storage domain. | [optional] 
**dedup** | **bool** | Specifies whether to enable dedup in storage domain. | [optional] 
**default_template_name** | **str** | Used for uniquely indentifying a default template. | [optional] [readonly] 
**id** | **int** | Specifies an id of the view template. | [optional] [readonly] 
**is_default** | **bool** | Specifies if the tempate is custom or static. | [optional] [readonly] 
**name** | **str** | Specifies the name of the view template. | [optional] 
**view_params** | [**CreateView**](CreateView.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.template import Template

# TODO update the JSON string below
json = "{}"
# create an instance of Template from a JSON string
template_instance = Template.from_json(json)
# print the JSON string representation of the object
print(Template.to_json())

# convert the object into a dict
template_dict = template_instance.to_dict()
# create an instance of Template from a dict
template_from_dict = Template.from_dict(template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


