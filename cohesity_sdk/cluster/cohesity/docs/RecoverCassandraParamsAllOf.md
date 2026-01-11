# RecoverCassandraParamsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshots** | [**[RecoverCassandraSnapshotParams], none_type**](RecoverCassandraSnapshotParams.md) | Specifies the local snapshot ids and other details of the Objects to be recovered. | 
**is_live_table_restore** | **bool, none_type** | Specifies whether the current recovery operation is a live table restore operation. | [optional] 
**is_system_keyspace_restore** | **bool, none_type** | Specifies whether the current recovery operation is a system keyspace restore operation. | [optional] 
**log_restore_directory** | **str, none_type** | Specifies the directory for restoring the logs. | [optional] 
**recover_privileges** | **bool, none_type** | Specifies whether recover/skip roles and permissions. | [optional] 
**restart_at_usecs** | **int, none_type** | Specifies the time in Unix epoch timestamp in microseconds at which the Cassandra services are to be restarted. | [optional] 
**restart_command** | **str, none_type** | Specifies the command to restart Cassandra services after the point in time recovery. | [optional] 
**restart_immediately** | **bool, none_type** | Specifies whether to restart Cassandra services immediately after the point in time recovery. | [optional] 
**restart_services** | **bool, none_type** | Specifies whether to restart Cassandra services after the point in time recovery. | [optional] 
**restart_services_task_id** | **int, none_type** | Specifies the Id of the task required to restart Cassandra services. | [optional] [readonly] 
**run_pre_checks** | **bool, none_type** | Specifies Whether to run checks before the recovery. E.x if there is sufficient space in the destination cluster for the recovery to succeed. | [optional] 
**selected_data_centers** | **[str]** | Selected Data centers for this cluster. | [optional] 
**staging_directory_list** | **[str]** | Specifies the directory on the primary to copy the files which are to be uploaded using destination sstableloader. | [optional] 
**suffix** | **str, none_type** | A suffix that is to be applied to all recovered objects. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


