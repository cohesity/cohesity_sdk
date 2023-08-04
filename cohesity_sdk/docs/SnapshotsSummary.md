# SnapshotsSummary

Specifies a summary of the object snapshots.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int, none_type** | Specifies the cluster id where the snapshots is stored. | [optional] 
**cluster_incarnation_id** | **int, none_type** | Specifies the cluster incarnation id where the snapshots is stored. | [optional] 
**region_id** | **str, none_type** | Specifies the cluster indentifier where the snapshots is stored. | [optional] 
**snapshot_target_type** | **str, none_type** | Specifies the target type where the Object&#39;s snapshot resides. | [optional] 
**external_target_info** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the external target information if this is an archival snapshot. | [optional] 
**snapshot_count** | **int, none_type** | Specifies the number of snapshots of this type and target. | [optional] 
**latest_snapshot_timestamp_usecs** | **int, none_type** | Specifies the timestamp in Unix time epoch in microseconds when the latest snapshot is taken. | [optional] 
**latest_run_start_time_usecs** | **int, none_type** | Specifies the timestamp in Unix time epoch in microseconds when the latest run started. | [optional] 
**latest_run_status** | **str, none_type** | Specifies the status of latest run. | [optional] 
**ownership_context** | **str, none_type** | Specifies the ownership context of the snapshot target. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


