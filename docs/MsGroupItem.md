# MsGroupItem

Specifies the indexed M365 Group item.

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
**mailbox_item** | [**Email**](Email.md) |  | [optional] 
**site_item** | [**DocumentLibraryItem**](DocumentLibraryItem.md) |  | [optional] 
**type** | **str** | Specifies the M365 Group item type. | [optional] 

## Example

```python
from cohesity_sdk.models.ms_group_item import MsGroupItem

# TODO update the JSON string below
json = "{}"
# create an instance of MsGroupItem from a JSON string
ms_group_item_instance = MsGroupItem.from_json(json)
# print the JSON string representation of the object
print(MsGroupItem.to_json())

# convert the object into a dict
ms_group_item_dict = ms_group_item_instance.to_dict()
# create an instance of MsGroupItem from a dict
ms_group_item_from_dict = MsGroupItem.from_dict(ms_group_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


