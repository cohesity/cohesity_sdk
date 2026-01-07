# DataAccessSession

Determines information about a specific data access session.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_time_usecs** | **int** | Specifies the time at which the session was created. | [optional] [readonly] 
**last_modification_time_usecs** | **int** | Specifies the time at which the session was last modified. | [optional] [readonly] 
**name** | **str, none_type** | The name of the data access session. | [optional] 
**session_id** | **str, none_type** | Specifies the id of the data access session. | [optional] 
**status** | **str** | Specifies the status of the Data Access Session. Machine status such as Admitted/WaitingForArchiveDownload/ WaitingForResource/SetupInProgress/Ready/Finished | [optional] 
**worker_endpoints** | [**[WorkerEndpoint], none_type**](WorkerEndpoint.md) | Specifies the list of metadata worker endpoints. In case of more than one metadata point client can contact any metadata worker. | [optional] 
**base_snapshot_info** | [**DataAccessSnapshotResponseParams**](DataAccessSnapshotResponseParams.md) |  | [optional] 
**current_snapshot_info** | [**DataAccessSnapshotResponseParams**](DataAccessSnapshotResponseParams.md) |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**source_id** | **int, none_type** | Specifies registered source id. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


