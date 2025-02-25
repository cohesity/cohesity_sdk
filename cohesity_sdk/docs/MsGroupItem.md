# MsGroupItem

Specifies the indexed M365 Group item.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the name of the object. | [optional] 
**path** | **str, none_type** | Specifies the path of the object. | [optional] 
**policy_id** | **str, none_type** | Specifies the protection policy id for this file. | [optional] 
**policy_name** | **str, none_type** | Specifies the protection policy name for this file. | [optional] 
**protection_group_id** | **str, none_type** | \&quot;Specifies the protection group id which contains this object.\&quot; | [optional] 
**protection_group_name** | **str, none_type** | \&quot;Specifies the protection group name which contains this object.\&quot; | [optional] 
**source_info** | [**ObjectSummary**](ObjectSummary.md) |  | [optional] 
**storage_domain_id** | **int, none_type** | \&quot;Specifies the Storage Domain id where the backup data of Object is present.\&quot; | [optional] 
**snapshot_tags** | [**[SnapshotTagInfo], none_type**](SnapshotTagInfo.md) | Specifies snapshot tags applied to the object. | [optional] 
**tags** | [**[TagInfo], none_type**](TagInfo.md) | Specifies tag applied to the object. | [optional] 
**mailbox_item** | [**Email**](Email.md) |  | [optional] 
**site_item** | [**DocumentLibraryItem**](DocumentLibraryItem.md) |  | [optional] 
**type** | **str, none_type** | Specifies the M365 Group item type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


