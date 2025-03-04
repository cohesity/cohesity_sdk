# PublicFolderItem

Specifies an Public folder indexed item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the name of the object. | [optional] 
**path** | **str** | Specifies the path of the object. | [optional] 
**policy_id** | **str** | Specifies the protection policy id for this file. | [optional] 
**policy_name** | **str** | Specifies the protection policy name for this file. | [optional] 
**protection_group_id** | **str** | \&quot;Specifies the protection group id which contains this object.\&quot; | [optional] 
**protection_group_name** | **str** | \&quot;Specifies the protection group name which contains this object.\&quot; | [optional] 
**source_info** | [**ObjectSummary**](ObjectSummary.md) |  | [optional] 
**storage_domain_id** | **int** | \&quot;Specifies the Storage Domain id where the backup data of Object is present.\&quot; | [optional] 
**snapshot_tags** | [**List[SnapshotTagInfo]**](SnapshotTagInfo.md) | Specifies snapshot tags applied to the object. | [optional] 
**tags** | [**List[TagInfo]**](TagInfo.md) | Specifies tag applied to the object. | [optional] 
**has_attachments** | **bool** | Specifies whether the item has any attachments | [optional] 
**id** | **str** | Specifies the id of the indexed item. | [optional] 
**item_class** | **str** | Specifies the item class of the indexed item. | [optional] 
**item_size** | **int** | Specifies the size in bytes for the indexed item. | [optional] 
**parent_folder_id** | **str** | Specifies the id of parent folder the indexed item. | [optional] 
**received_time_secs** | **int** | Specifies the Unix timestamp epoch in seconds at which this item is received. | [optional] 
**subject** | **str** | Specifies the subject of the indexed item. | [optional] 
**type** | **str** | Specifies the Public folder item type. | [optional] 

## Example

```python
from cohesity_sdk.models.public_folder_item import PublicFolderItem

# TODO update the JSON string below
json = "{}"
# create an instance of PublicFolderItem from a JSON string
public_folder_item_instance = PublicFolderItem.from_json(json)
# print the JSON string representation of the object
print(PublicFolderItem.to_json())

# convert the object into a dict
public_folder_item_dict = public_folder_item_instance.to_dict()
# create an instance of PublicFolderItem from a dict
public_folder_item_from_dict = PublicFolderItem.from_dict(public_folder_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


