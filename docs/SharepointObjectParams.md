# SharepointObjectParams

Specifies the common parameters for Sharepoint site objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_web_url** | **str** | Specifies the web url for the Sharepoint site. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.sharepoint_object_params import SharepointObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of SharepointObjectParams from a JSON string
sharepoint_object_params_instance = SharepointObjectParams.from_json(json)
# print the JSON string representation of the object
print(SharepointObjectParams.to_json())

# convert the object into a dict
sharepoint_object_params_dict = sharepoint_object_params_instance.to_dict()
# create an instance of SharepointObjectParams from a dict
sharepoint_object_params_from_dict = SharepointObjectParams.from_dict(sharepoint_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


