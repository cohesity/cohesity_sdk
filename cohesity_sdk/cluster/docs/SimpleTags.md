# SimpleTags

Specifies the simple tag parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Specifies key for the tag. | 
**value** | **str** | Specifies value for the tag. | 

## Example

```python
from cohesity_sdk.cluster.models.simple_tags import SimpleTags

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleTags from a JSON string
simple_tags_instance = SimpleTags.from_json(json)
# print the JSON string representation of the object
print(SimpleTags.to_json())

# convert the object into a dict
simple_tags_dict = simple_tags_instance.to_dict()
# create an instance of SimpleTags from a dict
simple_tags_from_dict = SimpleTags.from_dict(simple_tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


