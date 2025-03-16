# SnapshotDiffParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_snapshot_job_instance_id** | **int** |  | 
**base_snapshot_time_usecs** | **int** |  | 
**cluster_id** | **int** |  | 
**entity_type** | **str** |  | 
**incarnation_id** | **int** |  | [optional] 
**job_id** | **int** |  | 
**page_number** | **int** |  | 
**page_size** | **int** |  | 
**partition_id** | **int** |  | 
**snapshot_job_instance_id** | **int** |  | 
**snapshot_time_usecs** | **int** |  | 

## Example

```python
from cohesity_sdk.helios.models.snapshot_diff_params import SnapshotDiffParams

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotDiffParams from a JSON string
snapshot_diff_params_instance = SnapshotDiffParams.from_json(json)
# print the JSON string representation of the object
print(SnapshotDiffParams.to_json())

# convert the object into a dict
snapshot_diff_params_dict = snapshot_diff_params_instance.to_dict()
# create an instance of SnapshotDiffParams from a dict
snapshot_diff_params_from_dict = SnapshotDiffParams.from_dict(snapshot_diff_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


