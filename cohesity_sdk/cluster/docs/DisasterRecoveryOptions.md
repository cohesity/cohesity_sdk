# DisasterRecoveryOptions

Specifies the parameters that are needed for Disaster Recovery of a database to its production configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cleanup_original_db_files** | **bool, none_type** | Specifies whether to cleanup the original database files or to do precheck to ensure no conflicting files exists. Recovery will fail if there are any conflicting files. | [optional] 
**is_disaster_recovery** | **bool, none_type** | Specifies whether the recovery is of type Disaster Recovery. | [optional] 
**rename_database_asm_directory** | **bool, none_type** | Whether to rename the database ASM directory. If false, the adapter will leave the database files and continue with clone and migration of datafiles. This might cause extra files left behind on the Oracle host from the existing database instance. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


