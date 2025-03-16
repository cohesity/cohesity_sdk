# Snapshot

Snapshot identified by various parameters like clusterId, protectionGroupId, objectId etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Cluster Id of cluster to which this snapshot belongs. | 
**incarnation_id** | **int** | Incarnation id of cluster to which this snapshot belongs. | 
**object_id** | **int** | The snapshot is of this Object Id. | 
**protection_group_id** | **int** | Protection Group Id of protection group that created this snapshot. | 
**run_id** | **int** | Run Id of protection group run that created this snapshot. | [optional] 
**run_start_time_usecs** | **int** | Run start time (in microseconds) of protection group run that created this snapshot. | [optional] 
**snapshot_id** | **str** | Snapshot Id of this snapshot. | [optional] 
**tenant_ids** | **List[str]** | Tenant Ids associated with this snapshot, if any. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.snapshot import Snapshot

# TODO update the JSON string below
json = "{}"
# create an instance of Snapshot from a JSON string
snapshot_instance = Snapshot.from_json(json)
# print the JSON string representation of the object
print(Snapshot.to_json())

# convert the object into a dict
snapshot_dict = snapshot_instance.to_dict()
# create an instance of Snapshot from a dict
snapshot_from_dict = Snapshot.from_dict(snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


