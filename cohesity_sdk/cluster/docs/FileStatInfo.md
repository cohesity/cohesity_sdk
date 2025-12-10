# FileStatInfo

filestatInfo is the stat information for the file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_source_inode_id** | **int** | Source inode id metadata for certain adapters e.g. Netapp. | [optional] 
**modified_time_usecs** | **int** | If this is a file, the last modified time as returned by stat. | [optional] 
**one_drive_item_metadata** | [**OneDriveItemMetadata**](OneDriveItemMetadata.md) |  | [optional] 
**share_point_item_metadata** | [**SharepointItemMetadata**](SharepointItemMetadata.md) |  | [optional] 
**size** | **int** | If this is a file, the size of the file as returned by stat. This is Bytes | [optional] 
**type** | **str** | Specifies the file type. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.file_stat_info import FileStatInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FileStatInfo from a JSON string
file_stat_info_instance = FileStatInfo.from_json(json)
# print the JSON string representation of the object
print(FileStatInfo.to_json())

# convert the object into a dict
file_stat_info_dict = file_stat_info_instance.to_dict()
# create an instance of FileStatInfo from a dict
file_stat_info_from_dict = FileStatInfo.from_dict(file_stat_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


