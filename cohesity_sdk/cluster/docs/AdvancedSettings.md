# AdvancedSettings

This is used to regulate certain gflag values from the UI. The values passed by the user from the UI will be used for the respective gflags.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloned_db_backup_status** | **str, none_type** | Whether to report error if SQL database is cloned. | [optional] 
**db_backup_if_not_online_status** | **str, none_type** | Whether to report error if SQL database is not online. | [optional] 
**missing_db_backup_status** | **str, none_type** | Fail the backup job when the database is missing. The database may be missing if it is deleted or corrupted. | [optional] 
**offline_restoring_db_backup_status** | **str, none_type** | Fail the backup job when database is offline or restoring. | [optional] 
**read_only_db_backup_status** | **str, none_type** | Whether to skip backup for read-only SQL databases. | [optional] 
**report_all_non_autoprotect_db_errors** | **str, none_type** | Whether to report error for all dbs in non-autoprotect jobs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


