# PlatformSubTypeAgentImageInfo

Specifies the agent information of platform sub type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_url** | **str** | Specifies the URL for agent downlaod. | [optional] 
**package_type** | **str** | Specifies the package type of the agent. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.platform_sub_type_agent_image_info import PlatformSubTypeAgentImageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformSubTypeAgentImageInfo from a JSON string
platform_sub_type_agent_image_info_instance = PlatformSubTypeAgentImageInfo.from_json(json)
# print the JSON string representation of the object
print(PlatformSubTypeAgentImageInfo.to_json())

# convert the object into a dict
platform_sub_type_agent_image_info_dict = platform_sub_type_agent_image_info_instance.to_dict()
# create an instance of PlatformSubTypeAgentImageInfo from a dict
platform_sub_type_agent_image_info_from_dict = PlatformSubTypeAgentImageInfo.from_dict(platform_sub_type_agent_image_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


