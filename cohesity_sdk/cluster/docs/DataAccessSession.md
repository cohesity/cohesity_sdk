# DataAccessSession

Determines information about a specific data access session.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_time_usecs** | **int** | Specifies the time at which the session was created. | [optional] [readonly] 
**last_modification_time_usecs** | **int** | Specifies the time at which the session was last modified. | [optional] [readonly] 
**name** | **str** | The name of the data access session. | [optional] 
**session_id** | **str** | Specifies the id of the data access session. | [optional] 
**status** | **str** | Specifies the status of the Data Access Session. Machine status such as Admitted/WaitingForArchiveDownload/ WaitingForResource/SetupInProgress/Ready/Finished | [optional] 
**worker_endpoints** | [**List[WorkerEndpoint]**](WorkerEndpoint.md) | Specifies the list of metadata worker endpoints. In case of more than one metadata point client can contact any metadata worker. | [optional] 
**base_snapshot_info** | [**DataAccessSnapshotResponseParams**](DataAccessSnapshotResponseParams.md) |  | [optional] 
**current_snapshot_info** | [**DataAccessSnapshotResponseParams**](DataAccessSnapshotResponseParams.md) |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**source_id** | **int** | Specifies registered source id. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.data_access_session import DataAccessSession

# TODO update the JSON string below
json = "{}"
# create an instance of DataAccessSession from a JSON string
data_access_session_instance = DataAccessSession.from_json(json)
# print the JSON string representation of the object
print(DataAccessSession.to_json())

# convert the object into a dict
data_access_session_dict = data_access_session_instance.to_dict()
# create an instance of DataAccessSession from a dict
data_access_session_from_dict = DataAccessSession.from_dict(data_access_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


