# PhysicalVolumeProtectionGroupParams

Specifies the parameters which are specific to Volume based physical Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cobmr_backup** | **bool** | Specifies whether to take a CoBMR backup. | [optional] 
**continue_on_quiesce_failure** | **bool** | Specifies whether to continue backing up on quiesce failure | [optional] 
**dedup_exclusion_source_ids** | **List[int]** | Specifies ids of sources for which deduplication has to be disabled. | [optional] 
**excluded_vss_writers** | **List[str]** | Specifies writer names which should be excluded from physical volume based backups. | [optional] 
**incremental_backup_after_restart** | **bool** | Specifies whether or not to perform an incremental backup after the server restarts. This is applicable to windows environments. | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**objects** | [**List[PhysicalVolumeProtectionGroupObjectParams]**](PhysicalVolumeProtectionGroupObjectParams.md) |  | 
**perform_source_side_deduplication** | **bool** | Specifies whether or not to perform source side deduplication on this Protection Group. | [optional] 
**pre_post_script** | [**PrePostScriptParams**](PrePostScriptParams.md) |  | [optional] 
**quiesce** | **bool** | Specifies Whether to take app-consistent snapshots by quiescing apps and the filesystem before taking a backup | [optional] 

## Example

```python
from cohesity_sdk.models.physical_volume_protection_group_params import PhysicalVolumeProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalVolumeProtectionGroupParams from a JSON string
physical_volume_protection_group_params_instance = PhysicalVolumeProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(PhysicalVolumeProtectionGroupParams.to_json())

# convert the object into a dict
physical_volume_protection_group_params_dict = physical_volume_protection_group_params_instance.to_dict()
# create an instance of PhysicalVolumeProtectionGroupParams from a dict
physical_volume_protection_group_params_from_dict = PhysicalVolumeProtectionGroupParams.from_dict(physical_volume_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


