# DataAccessSnapshotResponseParams

Specifies the snapshot information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | Specifies the environment of the source. | [optional] 
**object_id** | **int** | Specifies the id of the object snapshot. | [optional] 
**point_in_time_usecs** | **int** | Specifies the timestamp (in microseconds. from epoch) for recovering to a point-in-time in the past. | [optional] 
**run_start_time_usecs** | **int** | Specifies the start time of the run in micro seconds. | [optional] 
**vault_id** | **int** | Specifies the id of the cluster vault. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.data_access_snapshot_response_params import DataAccessSnapshotResponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of DataAccessSnapshotResponseParams from a JSON string
data_access_snapshot_response_params_instance = DataAccessSnapshotResponseParams.from_json(json)
# print the JSON string representation of the object
print(DataAccessSnapshotResponseParams.to_json())

# convert the object into a dict
data_access_snapshot_response_params_dict = data_access_snapshot_response_params_instance.to_dict()
# create an instance of DataAccessSnapshotResponseParams from a dict
data_access_snapshot_response_params_from_dict = DataAccessSnapshotResponseParams.from_dict(data_access_snapshot_response_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


