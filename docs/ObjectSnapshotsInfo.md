# ObjectSnapshotsInfo

Specifies the snapshots information for every Protection Group for a given object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_snapshots_info** | [**[ObjectArchivalSnapshotInfo], none_type**](ObjectArchivalSnapshotInfo.md) | Specifies the archival snapshots information. | [optional] 
**indexing_status** | **str, none_type** | Specifies the indexing status of objects in this snapshot.&lt;br&gt; &#39;InProgress&#39; indicates the indexing is in progress.&lt;br&gt; &#39;Done&#39; indicates indexing is done.&lt;br&gt; &#39;NoIndex&#39; indicates indexing is not applicable.&lt;br&gt; &#39;Error&#39; indicates indexing failed with error. | [optional] 
**local_snapshot_info** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the local snapshot information. | [optional] 
**protection_group_id** | **str, none_type** | Specifies id of the Protection Group. | [optional] 
**protection_group_name** | **str, none_type** | Specifies name of the Protection Group. | [optional] 
**protection_run_end_time_usecs** | **int, none_type** | Specifies the end time of Protection Group Run in Unix timestamp epoch in microseconds. | [optional] 
**protection_run_id** | **str, none_type** | Specifies the id of Protection Group Run. | [optional] 
**protection_run_start_time_usecs** | **int, none_type** | Specifies the start time of Protection Group Run in Unix timestamp epoch in microseconds. | [optional] 
**run_instance_id** | **int, none_type** | Specifies the instance id of the protection run which create the snapshot. | [optional] 
**run_type** | **str, none_type** | Specifies the type of protection run created this snapshot. | [optional] 
**source_group_id** | **str, none_type** | Specifies the source protection group id in case of replication. | [optional] 
**storage_domain_id** | **int, none_type** | Specifies the Storage Domain id where the backup data of Object is present. | [optional] 
**storage_domain_name** | **str, none_type** | Specifies the name of Storage Domain id where the backup data of Object is present | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


