# ProgressStats

Specifies the stats within progress.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_file_count** | **int** | Specifies the total number of file and directory entities that are backed up in this run. Only applicable to file based backups. | [optional] 
**file_walk_done** | **bool** | Specifies whether the file system walk is done. Only applicable to file based backups. | [optional] 
**total_file_count** | **int** | Specifies the total number of file and directory entities visited in this backup. Only applicable to file based backups. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.progress_stats import ProgressStats

# TODO update the JSON string below
json = "{}"
# create an instance of ProgressStats from a JSON string
progress_stats_instance = ProgressStats.from_json(json)
# print the JSON string representation of the object
print(ProgressStats.to_json())

# convert the object into a dict
progress_stats_dict = progress_stats_instance.to_dict()
# create an instance of ProgressStats from a dict
progress_stats_from_dict = ProgressStats.from_dict(progress_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


