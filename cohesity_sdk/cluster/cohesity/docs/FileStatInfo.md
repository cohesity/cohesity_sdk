# FileStatInfo

filestatInfo is the stat information for the file.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_source_inode_id** | **int, none_type** | Source inode id metadata for certain adapters e.g. Netapp. | [optional] 
**modified_time_usecs** | **int, none_type** | If this is a file, the last modified time as returned by stat. | [optional] 
**one_drive_item_metadata** | [**OneDriveItemMetadata**](OneDriveItemMetadata.md) |  | [optional] 
**share_point_item_metadata** | [**SharepointItemMetadata**](SharepointItemMetadata.md) |  | [optional] 
**size** | **int, none_type** | If this is a file, the size of the file as returned by stat. This is Bytes | [optional] 
**type** | **str, none_type** | Specifies the file type. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


