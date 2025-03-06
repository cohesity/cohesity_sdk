# ViewsSummary

Get the summary of the Views.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_written_bytes** | **int** | Specifies the data written to all the views in bytes. | [optional] 
**data_written_bytes_prev** | **int** | Specifies the data written to all the views in bytes at a specific time. | [optional] 
**data_written_bytes_prev_timestamp_usec** | **int** | Specifies the timestamp in micro seconds when &#39;dataWrittenBytesPrev&#39; was calculated. | [optional] 
**data_written_bytes_timestamp_usec** | **int** | Specifies the timestamp in micro seconds when &#39;dataWrittenBytes&#39; was calculated. | [optional] 
**local_tier_resiliency_impact_bytes** | **int** | Specifies the size of the data that has been replicated to other nodes as per RF or Erasure Coding policy. | [optional] 
**local_tier_resiliency_impact_bytes_prev** | **int** | Specifies the size of the data that has been replicated to other nodes as per RF or Erasure Coding policy at a specific time. | [optional] 
**local_tier_resiliency_impact_bytes_prev_timestamp_usec** | **int** | Specifies the timestamp in micro seconds when &#39;localTierResiliencyImpactBytesPrev&#39; was calculated. | [optional] 
**local_tier_resiliency_impact_bytes_timestamp_usec** | **int** | Specifies the timestamp in micro seconds when &#39;localTierResiliencyImpactBytes&#39; was calculated. | [optional] 
**logical_usage_bytes** | **int** | Specifies the logical usage of all the views in bytes. | [optional] 
**logical_usage_bytes_prev** | **int** | Specifies the logical usage of all the views in bytes at a specific time. | [optional] 
**logical_usage_bytes_prev_timestamp_usec** | **int** | Specifies the timestamp in micro seconds when &#39;logicalUsageBytesPrev&#39; was calculated. | [optional] 
**logical_usage_bytes_timestamp_usec** | **int** | Specifies the timestamp in micro seconds when &#39;logicalUsageBytes&#39; was calculated. | [optional] 
**num_directories** | **int** | Specifies the number of directories. | [optional] 
**num_directories_prev** | **int** | Specifies the number of directories at a specific time. | [optional] 
**num_files** | **int** | Specifies the number of files. | [optional] 
**num_files_prev** | **int** | Specifies the number of files at a specific time. | [optional] 
**protected_views** | **int** | Specifies the number of all protected views. | [optional] 
**replicated_in_views** | **int** | Specifies the number of all the views that are replicated from remote clusters. | [optional] 
**replicated_out_views** | **int** | Specifies the number of all the views that are replicated out to remote clusters. | [optional] 
**storage_consumed_bytes** | **int** | Specifies the storage consumed of all the views in bytes. | [optional] 
**storage_consumed_bytes_prev** | **int** | Specifies the storage consumed by all the views in bytes at a specific time. | [optional] 
**storage_consumed_bytes_prev_timestamp_usec** | **int** | Specifies the timestamp in micro seconds when &#39;storageConsumedBytesPrev&#39; was calculated. | [optional] 
**storage_consumed_bytes_timestamp_usec** | **int** | Specifies the timestamp in micro seconds when &#39;storageConsumedBytes&#39; was calculated. | [optional] 
**total_views** | **int** | Specifies the number of all the views. | [optional] 
**view_entity_id** | **str** | Specifies the entity id of all the views. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.views_summary import ViewsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ViewsSummary from a JSON string
views_summary_instance = ViewsSummary.from_json(json)
# print the JSON string representation of the object
print(ViewsSummary.to_json())

# convert the object into a dict
views_summary_dict = views_summary_instance.to_dict()
# create an instance of ViewsSummary from a dict
views_summary_from_dict = ViewsSummary.from_dict(views_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


