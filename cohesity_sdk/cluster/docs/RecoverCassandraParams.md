# RecoverCassandraParams

Specifies the parameters to recover Cassandra objects.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshots** | [**[RecoverCassandraSnapshotParams], none_type**](RecoverCassandraSnapshotParams.md) | Specifies the local snapshot ids and other details of the Objects to be recovered. | 
**recover_to** | **int, none_type** | Specifies the &#39;Source Registration ID&#39; of the source where the objects are to be recovered. If this is not specified, the recovery job will recover to the original location. | [optional] 
**overwrite** | **bool, none_type** | Set to true to overwrite an existing object at the destination. If set to false, and the same object exists at the destination, then recovery will fail for that object. | [optional] 
**concurrency** | **int, none_type** | Specifies the maximum number of concurrent IO Streams that will be created to exchange data with the cluster. | [optional] 
**bandwidth_mbps** | **int, none_type** | Specifies the maximum network bandwidth that each concurrent IO Stream can use for exchanging data with the cluster. | [optional] 
**warnings** | **[str], none_type** | This field will hold the warnings in cases where the job status is SucceededWithWarnings. | [optional] [readonly] 
**suffix** | **str, none_type** | A suffix that is to be applied to all recovered objects. | [optional] 
**selected_data_centers** | **[str]** | Selected Data centers for this cluster. | [optional] 
**staging_directory_list** | **[str]** | Specifies the directory on the primary to copy the files which are to be uploaded using destination sstableloader. | [optional] 
**log_restore_directory** | **str, none_type** | Specifies the directory for restoring the logs. | [optional] 
**restart_services** | **bool, none_type** | Specifies whether to restart Cassandra services after the point in time recovery. | [optional] 
**restart_immediately** | **bool, none_type** | Specifies whether to restart Cassandra services immediately after the point in time recovery. | [optional] 
**restart_at_usecs** | **int, none_type** | Specifies the time in Unix epoch timestamp in microseconds at which the Cassandra services are to be restarted. | [optional] 
**restart_command** | **str, none_type** | Specifies the command to restart Cassandra services after the point in time recovery. | [optional] 
**restart_services_task_id** | **int, none_type** | Specifies the Id of the task requiered to restart Cassandra services. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


