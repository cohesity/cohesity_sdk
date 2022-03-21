# GetCopyStatParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_identifiers** | **[str], none_type** | This is a list of cluster identifiers to query snapshots for | [optional] 
**protection_group_ids** | **[str]** | This parameter applies if a single cluster is passed in cluster identifiers. | [optional] 
**run_instance_ids** | **[int]** | This parameter applies if a single cluster is passed in cluster identifiers. | [optional] 
**from_run_start_time_usecs** | **int** | Specifies the timestamp in Unix time epoch in microseconds to filter snapshots whose corresponding run started after this value. | [optional] 
**to_run_start_time_usecs** | **int** | Specifies the timestamp in Unix time epoch in microseconds to filter snapshots whose corresponding run started before this value. | [optional] 
**object_ids** | **[int]** | List of object ids to filter results. | [optional] 
**snapshot_ids** | **[str]** | List of snapshots Ids to filter result. | [optional] 
**tenant_ids** | **[str]** | List of tenant ids in an account. | [optional] 
**region_ids** | **[str]** | List of region Ids. | [optional] 
**tags** | [**[SnapshotTag]**](SnapshotTag.md) | List of tags to filter. | [optional] 
**has_anomaly_tag** | **bool, none_type** | This is a boolean to indicate if there are any anomaly tags on this run. | [optional] 
**locations** | **[str]** | This is to filter the type of runs to return. | [optional] 
**requested_data** | **[str]** | Filter out the type data requested per run. | [optional] 
**page_count** | **int, none_type** | Each result is returned in pages. This is the page number of the requested result. This parameters starts from 0. | [optional] 
**page_size** | **int, none_type** | The number of results to include in a page. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


