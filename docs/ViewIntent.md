# ViewIntent

Sepcifies the intent of the View.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_template_name** | **str** | Used for uniquely indentifying a default template | [optional] 
**template_id** | **int** | Specifies the template id from which the View is created. | [optional] 
**template_name** | **str** | Specifies the template name from which the View is created. | [optional] 

## Example

```python
from cohesity_sdk.models.view_intent import ViewIntent

# TODO update the JSON string below
json = "{}"
# create an instance of ViewIntent from a JSON string
view_intent_instance = ViewIntent.from_json(json)
# print the JSON string representation of the object
print(ViewIntent.to_json())

# convert the object into a dict
view_intent_dict = view_intent_instance.to_dict()
# create an instance of ViewIntent from a dict
view_intent_from_dict = ViewIntent.from_dict(view_intent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


