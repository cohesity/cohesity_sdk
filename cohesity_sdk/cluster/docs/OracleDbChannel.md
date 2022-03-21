# OracleDbChannel

Specifies the DB channel info for all the databases of app entity. Length of this array will be 1 for RAC and Standalone setups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_log_retention_days** | **int, none_type** | Specifies the number of days archive log should be stored. For keeping the archived log forever, set this to -1. For deleting the archived log immediately, set this to 0. For deleting the archived log after n days, set this to n. | [optional] 
**archive_log_retention_hours** | **int, none_type** | Specifies the number of hours archive log should be stored. For keeping the archived log forever, set this to -1. For deleting the archived log immediately, set this to 0. For deleting the archived log after k hours, set this to k. | [optional] 
**credentials** | [**Credentials**](Credentials.md) |  | [optional] 
**database_unique_name** | **str, none_type** | Specifies the unique Name of the database. | [optional] 
**database_uuid** | **str, none_type** | Specifies the database unique id. This is an internal field and is filled by magneto master based on corresponding app entity id. | [optional] 
**default_channel_count** | **int, none_type** | Specifies the default number of channels to use per node per database. This value is used on all Oracle Database Nodes unless databaseNodeList item&#39;s channelCount is specified for the node. Default value for the number of channels will be calculated as the minimum of number of nodes in Cohesity cluster and 2 * number of CPU on the host. If the number of channels is unspecified here and unspecified within databaseNodeList, the above formula will be used to determine the same. | [optional] 
**database_node_list** | [**[OracleDatabaseHost], none_type**](OracleDatabaseHost.md) | Specifies the Node info from where we are allowed to take the backup/restore. | [optional] 
**max_host_count** | **int, none_type** | Specifies the maximum number of hosts from which backup/restore is allowed in parallel. This will be less than or equal to the number of databaseNode specified within databaseNodeList. | [optional] 
**enable_dg_primary_backup** | **bool, none_type** | Specifies whether the database having the Primary role within Data Guard configuration is to be backed up. | [optional] 
**rman_backup_type** | **str** | Specifies the type of Oracle RMAN backup requested | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


