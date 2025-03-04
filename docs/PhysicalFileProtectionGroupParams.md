# PhysicalFileProtectionGroupParams

Specifies the parameters which are specific to Physical related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_parallel_runs** | **bool** | Specifies whether or not this job can have parallel runs. | [optional] 
**cobmr_backup** | **bool** | Specifies whether to take CoBMR backup. | [optional] 
**continue_on_quiesce_failure** | **bool** | Specifies whether to continue backing up on quiesce failure. | [optional] 
**dedup_exclusion_source_ids** | **List[int]** | Specifies ids of sources for which deduplication has to be disabled. | [optional] 
**excluded_vss_writers** | **List[str]** | Specifies writer names which should be excluded from physical file based backups. | [optional] 
**global_exclude_fs** | **List[str]** | Specifies global exclude filesystems which are applied to all sources in a job. | [optional] 
**global_exclude_paths** | **List[str]** | Specifies global exclude filters which are applied to all sources in a job. | [optional] 
**ignorable_errors** | **List[str]** | Specifies the Errors to be ignored in error db. | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**objects** | [**List[PhysicalFileProtectionGroupObjectParams]**](PhysicalFileProtectionGroupObjectParams.md) | Specifies the list of objects protected by this Protection Group. | 
**perform_brick_based_deduplication** | **bool** | Specifies whether or not to perform brick based deduplication on this Protection Group. | [optional] 
**perform_source_side_deduplication** | **bool** | Specifies whether or not to perform source side deduplication on this Protection Group. | [optional] 
**pre_post_script** | [**PrePostScriptParams**](PrePostScriptParams.md) |  | [optional] 
**quiesce** | **bool** | Specifies Whether to take app-consistent snapshots by quiescing apps and the filesystem before taking a backup. | [optional] 
**task_timeouts** | [**List[CancellationTimeoutParams]**](CancellationTimeoutParams.md) | Specifies the timeouts for all the objects inside this Protection Group, for both full and incremental backups. | [optional] 

## Example

```python
from cohesity_sdk.models.physical_file_protection_group_params import PhysicalFileProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalFileProtectionGroupParams from a JSON string
physical_file_protection_group_params_instance = PhysicalFileProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(PhysicalFileProtectionGroupParams.to_json())

# convert the object into a dict
physical_file_protection_group_params_dict = physical_file_protection_group_params_instance.to_dict()
# create an instance of PhysicalFileProtectionGroupParams from a dict
physical_file_protection_group_params_from_dict = PhysicalFileProtectionGroupParams.from_dict(physical_file_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


