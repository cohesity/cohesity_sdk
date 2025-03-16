# SnapshotsSummary

Specifies a summary of the object snapshots.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Specifies the cluster id where the snapshots is stored. | [optional] 
**cluster_incarnation_id** | **int** | Specifies the cluster incarnation id where the snapshots is stored. | [optional] 
**external_target_info** | [**ArchivalTargetSummaryInfo**](ArchivalTargetSummaryInfo.md) |  | [optional] 
**latest_run_start_time_usecs** | **int** | Specifies the timestamp in Unix time epoch in microseconds when the latest run started. | [optional] 
**latest_run_status** | **str** | Specifies the status of latest run. | [optional] 
**latest_snapshot_timestamp_usecs** | **int** | Specifies the timestamp in Unix time epoch in microseconds when the latest snapshot is taken. | [optional] 
**ownership_context** | **str** | Specifies the ownership context of the snapshot target. | [optional] 
**region_id** | **str** | Specifies the cluster indentifier where the snapshots is stored. | [optional] 
**snapshot_count** | **int** | Specifies the number of snapshots of this type and target. | [optional] 
**snapshot_target_type** | **str** | Specifies the target type where the Object&#39;s snapshot resides. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.snapshots_summary import SnapshotsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotsSummary from a JSON string
snapshots_summary_instance = SnapshotsSummary.from_json(json)
# print the JSON string representation of the object
print(SnapshotsSummary.to_json())

# convert the object into a dict
snapshots_summary_dict = snapshots_summary_instance.to_dict()
# create an instance of SnapshotsSummary from a dict
snapshots_summary_from_dict = SnapshotsSummary.from_dict(snapshots_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


