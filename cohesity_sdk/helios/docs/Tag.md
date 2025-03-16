# Tag

Tag details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_time_usecs** | **int** | Specifies the timestamp in microseconds since the epoch when this Tag was created. | [optional] [readonly] 
**description** | **str** | Description of the Tag. | [optional] 
**id** | **str** | Specifies unique id of the Tag. | [optional] [readonly] 
**last_updated_time_usecs** | **int** | Specifies the timestamp in microseconds since the epoch when this Tag was last updated. | [optional] [readonly] 
**marked_for_deletion** | **bool** | If true, Tag is marked for deletion. | [optional] [readonly] 
**name** | **str** | Name of the Tag. Name has to be unique under Namespace. | 
**namespace** | **str** | Namespace of the Tag. This is used to filter tags based on application or usecase. For example all tags related to vcenter can be put under one namespace or different departments could have their own namespaces e.g. finance/tag1 or operations/tag2 etc. | 
**tenant_id** | **str** | Tenant Id to whom the Tag belongs. | [optional] [readonly] 
**ui_color** | **str** | Color of the tag in UI. | [optional] 
**ui_path_elements** | **List[str]** | Path of the tag for UI nesting purposes. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.tag import Tag

# TODO update the JSON string below
json = "{}"
# create an instance of Tag from a JSON string
tag_instance = Tag.from_json(json)
# print the JSON string representation of the object
print(Tag.to_json())

# convert the object into a dict
tag_dict = tag_instance.to_dict()
# create an instance of Tag from a dict
tag_from_dict = Tag.from_dict(tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


