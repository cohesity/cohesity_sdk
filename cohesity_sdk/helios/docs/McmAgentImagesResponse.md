# McmAgentImagesResponse

Specifies the agent image information on Helios.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agents** | [**List[McmAgentImage]**](McmAgentImage.md) | Specifies a list of agents from Helios. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_agent_images_response import McmAgentImagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of McmAgentImagesResponse from a JSON string
mcm_agent_images_response_instance = McmAgentImagesResponse.from_json(json)
# print the JSON string representation of the object
print(McmAgentImagesResponse.to_json())

# convert the object into a dict
mcm_agent_images_response_dict = mcm_agent_images_response_instance.to_dict()
# create an instance of McmAgentImagesResponse from a dict
mcm_agent_images_response_from_dict = McmAgentImagesResponse.from_dict(mcm_agent_images_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


