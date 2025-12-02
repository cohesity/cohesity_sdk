# TagSet

Specifies tags for S3TaggingFilter property of AntivirusScanConfig. If any of the tags on the object matches any tags defined in tagSet array, it's regarded as a match.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Specifies the Key of the tag. | [optional] 
**value** | **str** | Specifies the Value of the tag. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.tag_set import TagSet

# TODO update the JSON string below
json = "{}"
# create an instance of TagSet from a JSON string
tag_set_instance = TagSet.from_json(json)
# print the JSON string representation of the object
print(TagSet.to_json())

# convert the object into a dict
tag_set_dict = tag_set_instance.to_dict()
# create an instance of TagSet from a dict
tag_set_from_dict = TagSet.from_dict(tag_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


