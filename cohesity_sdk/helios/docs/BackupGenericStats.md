# BackupGenericStats

Specifies the stats which are generic for all adapters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_ingested** | **int** | Specifies the amount of data which has been ingested in bytes. | [optional] 
**data_ingestion_rate** | **int** | Specifies the rate at which data is being ingested in bytes per minute. | [optional] 
**error_classes** | [**List[ErrorClass]**](ErrorClass.md) | Divides the errors into classes for better understanding for the user. | [optional] 
**estimated_backup_time** | **int** | Specifies the time in which backup should finish in minutes. | [optional] 
**num_errors** | **int** | Specifies the number of errors for this run. | [optional] 
**remaining_data_ingested** | **int** | Specifies the amount of data which has to be ingested in bytes. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.backup_generic_stats import BackupGenericStats

# TODO update the JSON string below
json = "{}"
# create an instance of BackupGenericStats from a JSON string
backup_generic_stats_instance = BackupGenericStats.from_json(json)
# print the JSON string representation of the object
print(BackupGenericStats.to_json())

# convert the object into a dict
backup_generic_stats_dict = backup_generic_stats_instance.to_dict()
# create an instance of BackupGenericStats from a dict
backup_generic_stats_from_dict = BackupGenericStats.from_dict(backup_generic_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


