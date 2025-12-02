# HeliosTagInfo

Specifies the helios tag info for an object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Specifies category of tag applied to the object. | [optional] 
**name** | **str** | Specifies name of tag applied to the object. | [optional] 
**sub_category** | **str** | Specifies subCategory of tag applied to the object. | [optional] 
**third_party_name** | **str** | Specifies thirdPartyName of tag applied to the object. | [optional] 
**type** | **str** | Specifies the type (ex custom, thirdparty, system) of tag applied to the object. | [optional] 
**ui_color** | **str** | Specifies the color of tag applied to the object. | [optional] 
**updated_time_usecs** | **int** | Specifies update time of tag applied to the object. | [optional] 
**uuid** | **str** | Specifies Uuid of tag applied to the object. | 

## Example

```python
from cohesity_sdk.cluster.models.helios_tag_info import HeliosTagInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosTagInfo from a JSON string
helios_tag_info_instance = HeliosTagInfo.from_json(json)
# print the JSON string representation of the object
print(HeliosTagInfo.to_json())

# convert the object into a dict
helios_tag_info_dict = helios_tag_info_instance.to_dict()
# create an instance of HeliosTagInfo from a dict
helios_tag_info_from_dict = HeliosTagInfo.from_dict(helios_tag_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


