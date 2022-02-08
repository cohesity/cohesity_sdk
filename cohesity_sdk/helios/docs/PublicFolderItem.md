# PublicFolderItem

Specifies an Public folder indexed item.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the name of the object. | [optional] 
**path** | **str, none_type** | Specifies the path of the object. | [optional] 
**protection_group_id** | **str, none_type** | \&quot;Specifies the protection group id which contains this object.\&quot; | [optional] 
**protection_group_name** | **str, none_type** | \&quot;Specifies the protection group name which contains this object.\&quot; | [optional] 
**storage_domain_id** | **int, none_type** | \&quot;Specifies the Storage Domain id where the backup data of Object   is present.\&quot; | [optional] 
**source_info** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the Source Object information. | [optional] 
**tags** | [**[TagInfo], none_type**](TagInfo.md) | Specifies tag applied to the object. | [optional] 
**snapshot_tags** | [**[SnapshotTagInfo], none_type**](SnapshotTagInfo.md) | Specifies snapshot tags applied to the object. | [optional] 
**type** | **str, none_type** | Specifies the Public folder item type. | [optional] 
**id** | **str, none_type** | Specifies the id of the indexed item. | [optional] 
**subject** | **str, none_type** | Specifies the subject of the indexed item. | [optional] 
**has_attachments** | **bool, none_type** | Specifies whether the item has any attachments | [optional] 
**item_class** | **str, none_type** | Specifies the item class of the indexed item. | [optional] 
**received_time_secs** | **int, none_type** | Specifies the Unix timestamp epoch in seconds at which this item is received. | [optional] 
**item_size** | **int, none_type** | Specifies the size in bytes for the indexed item. | [optional] 
**parent_folder_id** | **str, none_type** | Specifies the id of parent folder the indexed item. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


