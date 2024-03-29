# ExchangeRecoveryTargetConfig

Specifies the target object parameters to recover an Exchange database.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the id of the source to which the Exchange database will be recovered. | 
**database_name** | **str, none_type** | Specifies a new name for the restored database. | 
**database_directory_location** | **str, none_type** | Specifies the directory where to put the database data files. Missing directory will be automatically created. | 
**log_directory_location** | **str, none_type** | Specifies the directory where to put the database log files. Missing directory will be automatically created. | 
**mount_database** | **bool, none_type** | Specifies whether to mount the database after successful recovery. | [optional] 
**restore_as_recovery_db** | **bool, none_type** | Specifies whether to restore the Database as Recovery database. | [optional] 
**roll_forward_recovery** | **bool, none_type** | Specifies whether to use the latest logs on Exchange Server to perform roll-forward recovery. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


