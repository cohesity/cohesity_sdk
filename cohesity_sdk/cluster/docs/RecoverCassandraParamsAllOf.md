# RecoverCassandraParamsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshots** | [**[RecoverCassandraSnapshotParams], none_type**](RecoverCassandraSnapshotParams.md) | Specifies the local snapshot ids and other details of the Objects to be recovered. | 
**log_restore_directory** | **str, none_type** | Specifies the directory for restoring the logs. | [optional] 
**restart_at_usecs** | **int, none_type** | Specifies the time in Unix epoch timestamp in microseconds at which the Cassandra services are to be restarted. | [optional] 
**restart_command** | **str, none_type** | Specifies the command to restart Cassandra services after the point in time recovery. | [optional] 
**restart_immediately** | **bool, none_type** | Specifies whether to restart Cassandra services immediately after the point in time recovery. | [optional] 
**restart_services** | **bool, none_type** | Specifies whether to restart Cassandra services after the point in time recovery. | [optional] 
**restart_services_task_id** | **int, none_type** | Specifies the Id of the task requiered to restart Cassandra services. | [optional] [readonly] 
**selected_data_centers** | **[str]** | Selected Data centers for this cluster. | [optional] 
**staging_directory_list** | **[str]** | Specifies the directory on the primary to copy the files which are to be uploaded using destination sstableloader. | [optional] 
**suffix** | **str, none_type** | A suffix that is to be applied to all recovered objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


