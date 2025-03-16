# CustomTagParams

Specifies tag information of custom tags to be applied to various resources when converting and deploying a VM to AWS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Specifies key of the custom tag. | 
**value** | **str** | Specifies value of the custom tag. | 

## Example

```python
from cohesity_sdk.helios.models.custom_tag_params import CustomTagParams

# TODO update the JSON string below
json = "{}"
# create an instance of CustomTagParams from a JSON string
custom_tag_params_instance = CustomTagParams.from_json(json)
# print the JSON string representation of the object
print(CustomTagParams.to_json())

# convert the object into a dict
custom_tag_params_dict = custom_tag_params_instance.to_dict()
# create an instance of CustomTagParams from a dict
custom_tag_params_from_dict = CustomTagParams.from_dict(custom_tag_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


