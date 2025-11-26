# BackupGenericStats

Specifies the stats which are generic for all adapters.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_ingested** | **int, none_type** | Specifies the amount of data which has been ingested in bytes. | [optional] 
**data_ingestion_rate** | **int, none_type** | Specifies the rate at which data is being ingested in bytes per minute. | [optional] 
**error_classes** | [**[ErrorClass], none_type**](ErrorClass.md) | Divides the errors into classes for better understanding for the user. | [optional] 
**estimated_backup_time** | **int, none_type** | Specifies the time in which backup should finish in minutes. | [optional] 
**num_errors** | **int, none_type** | Specifies the number of errors for this run. | [optional] 
**remaining_data_ingested** | **int, none_type** | Specifies the amount of data which has to be ingested in bytes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


