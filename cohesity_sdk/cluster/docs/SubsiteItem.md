# SubsiteItem

Specifies a M365 Subsite item. Currently used for subsites of teams/group root site's subsites.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**absolute_item_path** | **str** | Specifies the unique path of the item as indexed by the document system. The path includes subsite IDs and document library IDs to ensure uniqueness. This property is only applicable to items within subsites. | [optional] 
**relative_subsite_path** | **str** | Specifies the relative path of this subsite item from subsite level. | [optional] 
**site_type** | **str** | Specifies the M365 Teams/Groups subsite item type. | [optional] 
**site_uuid** | **str** | Specifies the uuid of the site of the document library item. This is needed for Teams and Groups having subsites, as multiple items across different subsites can be selected for granular recovery. This is only applicable for the subsite items. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.subsite_item import SubsiteItem

# TODO update the JSON string below
json = "{}"
# create an instance of SubsiteItem from a JSON string
subsite_item_instance = SubsiteItem.from_json(json)
# print the JSON string representation of the object
print(SubsiteItem.to_json())

# convert the object into a dict
subsite_item_dict = subsite_item_instance.to_dict()
# create an instance of SubsiteItem from a dict
subsite_item_from_dict = SubsiteItem.from_dict(subsite_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


