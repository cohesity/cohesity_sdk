# TagAttributeParams

Specifies the tag attribute params to be associated with the entity created by the user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Specifies the key of the tag | [optional] 
**tag_type** | **str** | Specifies the information about tag type associated with the entity | 
**uuid** | **str** | Specifies the associated tag uuid | [optional] 
**value** | **str** | Specifies the value of the tag | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.tag_attribute_params import TagAttributeParams

# TODO update the JSON string below
json = "{}"
# create an instance of TagAttributeParams from a JSON string
tag_attribute_params_instance = TagAttributeParams.from_json(json)
# print the JSON string representation of the object
print(TagAttributeParams.to_json())

# convert the object into a dict
tag_attribute_params_dict = tag_attribute_params_instance.to_dict()
# create an instance of TagAttributeParams from a dict
tag_attribute_params_from_dict = TagAttributeParams.from_dict(tag_attribute_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


