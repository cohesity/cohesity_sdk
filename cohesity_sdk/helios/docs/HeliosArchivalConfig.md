# HeliosArchivalConfig

Specifies settings for copying Snapshots External Targets (such as AWS or Tape). This also specifies the retention policy that should be applied to Snapshots after they have been copied to the specified target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_id** | **str** | Specifies the unique identifier for the target getting added. This field need to be passed only when helios policies are updated. | [optional] 
**copy_on_run_success** | **bool** | Specifies if Snapshots are copied from the first completely successful Protection Group Run or the first partially successful Protection Group Run occurring at the start of the replication schedule. &lt;br&gt; If true, Snapshots are copied from the first Protection Group Run occurring at the start of the replication schedule that was completely successful i.e. Snapshots for all the Objects in the Protection Group were successfully captured. &lt;br&gt; If false, Snapshots are copied from the first Protection Group Run occurring at the start of the replication schedule, even if first Protection Group Run was not completely successful i.e. Snapshots were not captured for all Objects in the Protection Group. | [optional] 
**retention** | [**HeliosRetention**](HeliosRetention.md) |  | [optional] 
**schedule** | [**HeliosTargetSchedule**](HeliosTargetSchedule.md) |  | [optional] 
**extended_retention** | [**List[HeliosExtendedRetentionPolicy]**](HeliosExtendedRetentionPolicy.md) | Specifies additional retention policies that should be applied to the archived backup. Archived backup snapshot will be retained up to a time that is the maximum of all retention policies that are applicable to it. | [optional] 
**target_id** | **int** | Specifies the Archival target to copy the Snapshots to. | 
**target_name** | **str** | Specifies the Archival target name where Snapshots are copied. | [optional] [readonly] 
**target_type** | **str** | Specifies the Archival target type where Snapshots are copied. | [optional] [readonly] 
**tier_settings** | [**HeliosTierLevelSettings**](HeliosTierLevelSettings.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_archival_config import HeliosArchivalConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosArchivalConfig from a JSON string
helios_archival_config_instance = HeliosArchivalConfig.from_json(json)
# print the JSON string representation of the object
print(HeliosArchivalConfig.to_json())

# convert the object into a dict
helios_archival_config_dict = helios_archival_config_instance.to_dict()
# create an instance of HeliosArchivalConfig from a dict
helios_archival_config_from_dict = HeliosArchivalConfig.from_dict(helios_archival_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


