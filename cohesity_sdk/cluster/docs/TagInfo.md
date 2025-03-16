# TagInfo

Specifies the tag info for an object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_id** | **str** | Specifies Id of tag applied to the object. | 

## Example

```python
from cohesity_sdk.cluster.models.tag_info import TagInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TagInfo from a JSON string
tag_info_instance = TagInfo.from_json(json)
# print the JSON string representation of the object
print(TagInfo.to_json())

# convert the object into a dict
tag_info_dict = tag_info_instance.to_dict()
# create an instance of TagInfo from a dict
tag_info_from_dict = TagInfo.from_dict(tag_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


