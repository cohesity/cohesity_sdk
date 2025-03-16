# TaggingInfo

Specifies the tagging config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_restore** | **bool** | Specifies if blocking restore operations from snapshots with specified tag is enabled or not. | [optional] 
**tag_id** | **int** | Specifies the id of the tag used to identify which snapshots to block restore from. | [optional] 
**tag_name** | **str** | Specifies the label of the tag used to identify which snapshots to block restore from. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.tagging_info import TaggingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TaggingInfo from a JSON string
tagging_info_instance = TaggingInfo.from_json(json)
# print the JSON string representation of the object
print(TaggingInfo.to_json())

# convert the object into a dict
tagging_info_dict = tagging_info_instance.to_dict()
# create an instance of TaggingInfo from a dict
tagging_info_from_dict = TaggingInfo.from_dict(tagging_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


