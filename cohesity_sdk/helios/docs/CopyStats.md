# CopyStats

Specifies the stats for all the copies of this backup run.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_metrics** | [**StorageMetrics**](StorageMetrics.md) |  | [optional] 
**indexing_stats** | [**IndexingStats**](IndexingStats.md) |  | [optional] 
**tagging_info** | [**Tags**](Tags.md) |  | [optional] 
**file_extensions** | [**FileExtensions**](FileExtensions.md) |  | [optional] 
**anomaly_status** | [**AnomalyStatus**](AnomalyStatus.md) |  | [optional] 
**page_count** | **int, none_type** | The page count of this response. | [optional] 
**page_size** | **int, none_type** | The page size of this result. | [optional] 
**local** | [**LocalCopy**](LocalCopy.md) |  | [optional] 
**archivals** | [**[ArchivalCopy]**](ArchivalCopy.md) | This contains the details of the archival copies of the run. | [optional] 
**replications** | [**[ReplicationCopy]**](ReplicationCopy.md) | Replication copies of the run. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


