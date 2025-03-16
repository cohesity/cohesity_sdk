# TeamsItem

Specifies the indexed M365 Teams item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the name of the object. | [optional] 
**path** | **str** | Specifies the path of the object. | [optional] 
**policy_id** | **str** | Specifies the protection policy id for this file. | [optional] 
**policy_name** | **str** | Specifies the protection policy name for this file. | [optional] 
**protection_group_id** | **str** | \&quot;Specifies the protection group id which contains this object.\&quot; | [optional] 
**protection_group_name** | **str** | \&quot;Specifies the protection group name which contains this object.\&quot; | [optional] 
**source_info** | **object** | Specifies the Source Object information. | [optional] 
**storage_domain_id** | **int** | \&quot;Specifies the Storage Domain id where the backup data of Object is present.\&quot; | [optional] 
**snapshot_tags** | [**List[SnapshotTagInfo]**](SnapshotTagInfo.md) | Specifies snapshot tags applied to the object. | [optional] 
**tags** | [**List[TagInfo]**](TagInfo.md) | Specifies tag applied to the object. | [optional] 
**channel_item** | [**ChannelItem**](ChannelItem.md) |  | [optional] 
**file_item** | [**TeamsFileItem**](TeamsFileItem.md) |  | [optional] 
**type** | **str** | Specifies the M365 Teams item type. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.teams_item import TeamsItem

# TODO update the JSON string below
json = "{}"
# create an instance of TeamsItem from a JSON string
teams_item_instance = TeamsItem.from_json(json)
# print the JSON string representation of the object
print(TeamsItem.to_json())

# convert the object into a dict
teams_item_dict = teams_item_instance.to_dict()
# create an instance of TeamsItem from a dict
teams_item_from_dict = TeamsItem.from_dict(teams_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


