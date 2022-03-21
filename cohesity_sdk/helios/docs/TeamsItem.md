# TeamsItem

Specifies the indexed M365 Teams item.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the name of the object. | [optional] 
**path** | **str, none_type** | Specifies the path of the object. | [optional] 
**protection_group_id** | **str, none_type** | \&quot;Specifies the protection group id which contains this object.\&quot; | [optional] 
**protection_group_name** | **str, none_type** | \&quot;Specifies the protection group name which contains this object.\&quot; | [optional] 
**policy_id** | **str, none_type** | Specifies the protection policy id for this file. | [optional] 
**policy_name** | **str, none_type** | Specifies the protection policy name for this file. | [optional] 
**storage_domain_id** | **int, none_type** | \&quot;Specifies the Storage Domain id where the backup data of Object is present.\&quot; | [optional] 
**source_info** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the Source Object information. | [optional] 
**tags** | [**[TagInfo], none_type**](TagInfo.md) | Specifies tag applied to the object. | [optional] 
**snapshot_tags** | [**[SnapshotTagInfo], none_type**](SnapshotTagInfo.md) | Specifies snapshot tags applied to the object. | [optional] 
**type** | **str, none_type** | Specifies the M365 Teams item type. | [optional] 
**channel_item** | [**ChannelItem**](ChannelItem.md) |  | [optional] 
**file_item** | [**TeamsFileItem**](TeamsFileItem.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


