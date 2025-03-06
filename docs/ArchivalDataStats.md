# ArchivalDataStats

Specifies statistics about archival data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_logical_transfer_rate_bps** | **int** | Specifies the average rate of transfer in bytes per second. | [optional] 
**backup_file_count** | **int** | Specifies the total number of file and directory entities that are backed up in this run. Only applicable to file based backups. | [optional] 
**bytes_read** | **int** | Specifies total logical bytes read for creating the snapshot. | [optional] 
**file_walk_done** | **bool** | Specifies whether the file system walk is done. Only applicable to file based backups. | [optional] 
**logical_bytes_transferred** | **int** | Specifies the logical bytes transferred. | [optional] 
**logical_size_bytes** | **int** | Specifies the logicalSizeBytes. | [optional] 
**physical_bytes_transferred** | **int** | Specifies the physical bytes transferred. | [optional] 
**total_file_count** | **int** | Specifies the total number of file and directory entities visited in this backup. Only applicable to file based backups. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.archival_data_stats import ArchivalDataStats

# TODO update the JSON string below
json = "{}"
# create an instance of ArchivalDataStats from a JSON string
archival_data_stats_instance = ArchivalDataStats.from_json(json)
# print the JSON string representation of the object
print(ArchivalDataStats.to_json())

# convert the object into a dict
archival_data_stats_dict = archival_data_stats_instance.to_dict()
# create an instance of ArchivalDataStats from a dict
archival_data_stats_from_dict = ArchivalDataStats.from_dict(archival_data_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


