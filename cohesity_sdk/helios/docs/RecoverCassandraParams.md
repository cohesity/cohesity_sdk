# RecoverCassandraParams

Specifies the parameters to recover Cassandra objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advanced_configs** | [**List[KeyValuePair]**](KeyValuePair.md) | Specifies the advanced configuration for a recovery job. | [optional] 
**bandwidth_mbps** | **int** | Specifies the maximum network bandwidth that each concurrent IO Stream can use for exchanging data with the cluster. | [optional] 
**concurrency** | **int** | Specifies the maximum number of concurrent IO Streams that will be created to exchange data with the cluster. | [optional] 
**overwrite** | **bool** | Set to true to overwrite an existing object at the destination. If set to false, and the same object exists at the destination, then recovery will fail for that object. | [optional] 
**recover_to** | **int** | Specifies the &#39;Source Registration ID&#39; of the source where the objects are to be recovered. If this is not specified, the recovery job will recover to the original location. | [optional] 
**warnings** | **List[str]** | This field will hold the warnings in cases where the job status is SucceededWithWarnings. | [optional] [readonly] 
**is_live_table_restore** | **bool** | Specifies whether the current recovery operation is a live table restore operation. | [optional] 
**is_system_keyspace_restore** | **bool** | Specifies whether the current recovery operation is a system keyspace restore operation. | [optional] 
**log_restore_directory** | **str** | Specifies the directory for restoring the logs. | [optional] 
**recover_privileges** | **bool** | Specifies whether recover/skip roles and permissions. | [optional] 
**restart_at_usecs** | **int** | Specifies the time in Unix epoch timestamp in microseconds at which the Cassandra services are to be restarted. | [optional] 
**restart_command** | **str** | Specifies the command to restart Cassandra services after the point in time recovery. | [optional] 
**restart_immediately** | **bool** | Specifies whether to restart Cassandra services immediately after the point in time recovery. | [optional] 
**restart_services** | **bool** | Specifies whether to restart Cassandra services after the point in time recovery. | [optional] 
**restart_services_task_id** | **int** | Specifies the Id of the task required to restart Cassandra services. | [optional] [readonly] 
**selected_data_centers** | **List[str]** | Selected Data centers for this cluster. | [optional] 
**snapshots** | [**List[RecoverCassandraSnapshotParams]**](RecoverCassandraSnapshotParams.md) | Specifies the local snapshot ids and other details of the Objects to be recovered. | 
**staging_directory_list** | **List[str]** | Specifies the directory on the primary to copy the files which are to be uploaded using destination sstableloader. | [optional] 
**suffix** | **str** | A suffix that is to be applied to all recovered objects. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.recover_cassandra_params import RecoverCassandraParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverCassandraParams from a JSON string
recover_cassandra_params_instance = RecoverCassandraParams.from_json(json)
# print the JSON string representation of the object
print(RecoverCassandraParams.to_json())

# convert the object into a dict
recover_cassandra_params_dict = recover_cassandra_params_instance.to_dict()
# create an instance of RecoverCassandraParams from a dict
recover_cassandra_params_from_dict = RecoverCassandraParams.from_dict(recover_cassandra_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


