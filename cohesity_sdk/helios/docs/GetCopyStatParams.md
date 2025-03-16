# GetCopyStatParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_identifiers** | **List[str]** | This is a list of cluster identifiers to query snapshots for | [optional] 
**from_run_start_time_usecs** | **int** | Specifies the timestamp in Unix time epoch in microseconds to filter snapshots whose corresponding run started after this value. | [optional] 
**has_anomaly_tag** | **bool** | This is a boolean to indicate if there are any anomaly tags on this run. | [optional] 
**locations** | **List[str]** | This is to filter the type of runs to return. | [optional] 
**object_ids** | **List[int]** | List of object ids to filter results. | [optional] 
**page_count** | **int** | Each result is returned in pages. This is the page number of the requested result. This parameters starts from 0. | [optional] 
**page_size** | **int** | The number of results to include in a page. | [optional] 
**protection_group_ids** | **List[str]** | This parameter applies if a single cluster is passed in cluster identifiers. | [optional] 
**region_ids** | **List[str]** | List of region Ids. | [optional] 
**requested_data** | **List[str]** | Filter out the type data requested per run. | [optional] 
**run_instance_ids** | **List[int]** | This parameter applies if a single cluster is passed in cluster identifiers. | [optional] 
**snapshot_ids** | **List[str]** | List of snapshots Ids to filter result. | [optional] 
**tags** | [**List[SnapshotTag]**](SnapshotTag.md) | List of tags to filter. | [optional] 
**tenant_ids** | **List[str]** | List of tenant ids in an account. | [optional] 
**to_run_start_time_usecs** | **int** | Specifies the timestamp in Unix time epoch in microseconds to filter snapshots whose corresponding run started before this value. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.get_copy_stat_params import GetCopyStatParams

# TODO update the JSON string below
json = "{}"
# create an instance of GetCopyStatParams from a JSON string
get_copy_stat_params_instance = GetCopyStatParams.from_json(json)
# print the JSON string representation of the object
print(GetCopyStatParams.to_json())

# convert the object into a dict
get_copy_stat_params_dict = get_copy_stat_params_instance.to_dict()
# create an instance of GetCopyStatParams from a dict
get_copy_stat_params_from_dict = GetCopyStatParams.from_dict(get_copy_stat_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


