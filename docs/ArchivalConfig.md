# ArchivalConfig

Specifies settings for copying Snapshots External Targets (such as AWS or Tape). This also specifies the retention policy that should be applied to Snapshots after they have been copied to the specified target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_run_type** | **str** | Specifies which type of run should be copied, if not set, all types of runs will be eligible for copying. If set, this will ensure that the first run of given type in the scheduled period will get copied. Currently, this can only be set to Full. | [optional] 
**config_id** | **str** | Specifies the unique identifier for the target getting added. This field need to be passed only when policies are being updated. | [optional] 
**copy_on_run_success** | **bool** | Specifies if Snapshots are copied from the first completely successful Protection Group Run or the first partially successful Protection Group Run occurring at the start of the replication schedule. &lt;br&gt; If true, Snapshots are copied from the first Protection Group Run occurring at the start of the replication schedule that was completely successful i.e. Snapshots for all the Objects in the Protection Group were successfully captured. &lt;br&gt; If false, Snapshots are copied from the first Protection Group Run occurring at the start of the replication schedule, even if first Protection Group Run was not completely successful i.e. Snapshots were not captured for all Objects in the Protection Group. | [optional] 
**log_retention** | [**LogRetention**](LogRetention.md) |  | [optional] 
**retention** | [**Retention**](Retention.md) |  | 
**run_timeouts** | [**List[CancellationTimeoutParams]**](CancellationTimeoutParams.md) | Specifies the replication/archival timeouts for different type of runs(kFull, kRegular etc.). | [optional] 
**schedule** | [**TargetSchedule**](TargetSchedule.md) |  | 
**extended_retention** | [**List[ExtendedRetentionPolicy]**](ExtendedRetentionPolicy.md) | Specifies additional retention policies that should be applied to the archived backup. Archived backup snapshot will be retained up to a time that is the maximum of all retention policies that are applicable to it. | [optional] 
**target_id** | **int** | Specifies the Archival target to copy the Snapshots to. | 
**target_name** | **str** | Specifies the Archival target name where Snapshots are copied. | [optional] [readonly] 
**target_type** | **str** | Specifies the Archival target type where Snapshots are copied. | [optional] [readonly] 
**tier_settings** | [**TierLevelSettings**](TierLevelSettings.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.archival_config import ArchivalConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArchivalConfig from a JSON string
archival_config_instance = ArchivalConfig.from_json(json)
# print the JSON string representation of the object
print(ArchivalConfig.to_json())

# convert the object into a dict
archival_config_dict = archival_config_instance.to_dict()
# create an instance of ArchivalConfig from a dict
archival_config_from_dict = ArchivalConfig.from_dict(archival_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


