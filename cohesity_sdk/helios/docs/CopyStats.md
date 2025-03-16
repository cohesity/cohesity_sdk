# CopyStats

Specifies the stats for all the copies of this backup run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anomaly_status** | [**AnomalyStatus**](AnomalyStatus.md) |  | [optional] 
**archivals** | [**List[ArchivalCopy]**](ArchivalCopy.md) | This contains the details of the archival copies of the run. | [optional] 
**file_extensions** | [**List[FileExtensionDetails]**](FileExtensionDetails.md) |  | [optional] 
**indexing_stats** | [**IndexingStats**](IndexingStats.md) |  | [optional] 
**local** | [**LocalCopy**](LocalCopy.md) |  | [optional] 
**page_count** | **int** | The page count of this response. | [optional] 
**page_size** | **int** | The page size of this result. | [optional] 
**replications** | [**List[ReplicationCopy]**](ReplicationCopy.md) | Replication copies of the run. | [optional] 
**storage_metrics** | [**StorageMetrics**](StorageMetrics.md) |  | [optional] 
**tagging_info** | [**Tags**](Tags.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.copy_stats import CopyStats

# TODO update the JSON string below
json = "{}"
# create an instance of CopyStats from a JSON string
copy_stats_instance = CopyStats.from_json(json)
# print the JSON string representation of the object
print(CopyStats.to_json())

# convert the object into a dict
copy_stats_dict = copy_stats_instance.to_dict()
# create an instance of CopyStats from a dict
copy_stats_from_dict = CopyStats.from_dict(copy_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


