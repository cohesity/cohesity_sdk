# DataAccessSnapshotInfo

Specifies the snapshot information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | Specifies the environment of the source. | 
**restore_time_usecs** | **int** | Specifies the time to which the object needs to be restored. If this is not specified the object is restore from the base snapshot identified by the run_start_time_usecs. | [optional] 
**snapshot_id** | **str** | Specifies the id of the object snapshot. | 

## Example

```python
from cohesity_sdk.cluster.models.data_access_snapshot_info import DataAccessSnapshotInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataAccessSnapshotInfo from a JSON string
data_access_snapshot_info_instance = DataAccessSnapshotInfo.from_json(json)
# print the JSON string representation of the object
print(DataAccessSnapshotInfo.to_json())

# convert the object into a dict
data_access_snapshot_info_dict = data_access_snapshot_info_instance.to_dict()
# create an instance of DataAccessSnapshotInfo from a dict
data_access_snapshot_info_from_dict = DataAccessSnapshotInfo.from_dict(data_access_snapshot_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


