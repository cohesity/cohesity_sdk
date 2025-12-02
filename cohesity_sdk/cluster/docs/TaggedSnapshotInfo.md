# TaggedSnapshotInfo

Specifies helios tagged related snapshot info for an object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Specifies the cluster Id of the tagged snapshot. | [optional] 
**cluster_incarnation_id** | **int** | Specifies the clusterIncarnationId of the tagged snapshot. | [optional] 
**job_id** | **int** | Specifies the jobId of the tagged snapshot. | [optional] 
**object_uuid** | **str** | Specifies the object uuid of the tagged snapshot. | [optional] 
**run_start_time_usecs** | **int** | Specifies the runStartTimeUsecs of the tagged snapshot. | [optional] 
**tags** | [**List[HeliosTagInfo]**](HeliosTagInfo.md) | Specifies tag applied to the object. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.tagged_snapshot_info import TaggedSnapshotInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TaggedSnapshotInfo from a JSON string
tagged_snapshot_info_instance = TaggedSnapshotInfo.from_json(json)
# print the JSON string representation of the object
print(TaggedSnapshotInfo.to_json())

# convert the object into a dict
tagged_snapshot_info_dict = tagged_snapshot_info_instance.to_dict()
# create an instance of TaggedSnapshotInfo from a dict
tagged_snapshot_info_from_dict = TaggedSnapshotInfo.from_dict(tagged_snapshot_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


