# BackupDataStats

Specifies statistics about local snapshot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes_read** | **int** | Specifies total logical bytes read for creating the snapshot. | [optional] 
**bytes_written** | **int** | Specifies total size of data in bytes written after taking backup. | [optional] 
**logical_size_bytes** | **int** | Specifies total logical size of object(s) in bytes. | [optional] 

## Example

```python
from cohesity_sdk.models.backup_data_stats import BackupDataStats

# TODO update the JSON string below
json = "{}"
# create an instance of BackupDataStats from a JSON string
backup_data_stats_instance = BackupDataStats.from_json(json)
# print the JSON string representation of the object
print(BackupDataStats.to_json())

# convert the object into a dict
backup_data_stats_dict = backup_data_stats_instance.to_dict()
# create an instance of BackupDataStats from a dict
backup_data_stats_from_dict = BackupDataStats.from_dict(backup_data_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


