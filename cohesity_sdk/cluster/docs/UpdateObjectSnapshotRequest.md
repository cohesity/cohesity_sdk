# UpdateObjectSnapshotRequest

Specifies the parameters to update an object snapshot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_lock_type** | **str** | Specifies the snapshot data lock type. | [optional] 
**expiry_time_secs** | **int** | Specifies the expiry time of the snapshot in Unix timestamp epoch in seconds. | [optional] 
**set_legal_hold** | **bool** | Whether to set the snapshot on legal hold. If set to true, the run cannot be deleted during the retention period. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.update_object_snapshot_request import UpdateObjectSnapshotRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateObjectSnapshotRequest from a JSON string
update_object_snapshot_request_instance = UpdateObjectSnapshotRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateObjectSnapshotRequest.to_json())

# convert the object into a dict
update_object_snapshot_request_dict = update_object_snapshot_request_instance.to_dict()
# create an instance of UpdateObjectSnapshotRequest from a dict
update_object_snapshot_request_from_dict = UpdateObjectSnapshotRequest.from_dict(update_object_snapshot_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


