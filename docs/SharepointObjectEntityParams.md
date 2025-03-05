# SharepointObjectEntityParams

Specifies the common parameters for Sharepoint site objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_web_url** | **str** | Specifies the web url for the Sharepoint site. | [optional] 

## Example

```python
from cohesity_sdk.models.sharepoint_object_entity_params import SharepointObjectEntityParams

# TODO update the JSON string below
json = "{}"
# create an instance of SharepointObjectEntityParams from a JSON string
sharepoint_object_entity_params_instance = SharepointObjectEntityParams.from_json(json)
# print the JSON string representation of the object
print(SharepointObjectEntityParams.to_json())

# convert the object into a dict
sharepoint_object_entity_params_dict = sharepoint_object_entity_params_instance.to_dict()
# create an instance of SharepointObjectEntityParams from a dict
sharepoint_object_entity_params_from_dict = SharepointObjectEntityParams.from_dict(sharepoint_object_entity_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


