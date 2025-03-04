# BackupNasStats

Specifies the stats which are specific for NAS adapter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_analysis_rate** | **int** | Specifies the rate at which files are being analyzed in files per minute. | [optional] 
**file_discovery_rate** | **int** | Specifies the rate at which files are being discovered in files per minute. | [optional] 
**file_discovery_time** | **int** | Specifies the time taken for file discovery. | [optional] 
**file_ingestion_rate** | **int** | Specifies the rate at which files are being ingested in files per minute. | [optional] 
**files_analyzed** | **int** | Specifies the number of files which have been analyzed. | [optional] 
**files_discovered** | **int** | Specifies the number of files which have already been discovered. | [optional] 
**files_ingested** | **int** | Specifies the number of files which have been ingested. | [optional] 
**walker_run_time** | **int** | Specifies the run time for directory walker in seconds. | [optional] 

## Example

```python
from cohesity_sdk.models.backup_nas_stats import BackupNasStats

# TODO update the JSON string below
json = "{}"
# create an instance of BackupNasStats from a JSON string
backup_nas_stats_instance = BackupNasStats.from_json(json)
# print the JSON string representation of the object
print(BackupNasStats.to_json())

# convert the object into a dict
backup_nas_stats_dict = backup_nas_stats_instance.to_dict()
# create an instance of BackupNasStats from a dict
backup_nas_stats_from_dict = BackupNasStats.from_dict(backup_nas_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


