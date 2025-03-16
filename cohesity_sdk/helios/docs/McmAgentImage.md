# McmAgentImage

Specifies the agent image information on Helios.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_sub_types** | [**List[PlatformSubTypeAgentImageInfo]**](PlatformSubTypeAgentImageInfo.md) | Specifies the agent information of platform subtypes. | [optional] 
**download_url** | **str** | Specifies the URL for agent downlaod. | [optional] 
**platform** | **str** | Specifies the type of the agent platform. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_agent_image import McmAgentImage

# TODO update the JSON string below
json = "{}"
# create an instance of McmAgentImage from a JSON string
mcm_agent_image_instance = McmAgentImage.from_json(json)
# print the JSON string representation of the object
print(McmAgentImage.to_json())

# convert the object into a dict
mcm_agent_image_dict = mcm_agent_image_instance.to_dict()
# create an instance of McmAgentImage from a dict
mcm_agent_image_from_dict = McmAgentImage.from_dict(mcm_agent_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


