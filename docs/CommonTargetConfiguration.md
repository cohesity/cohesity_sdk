# CommonTargetConfiguration

Specifies common parameters required while setting up additional protection target configuration.

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

## Example

```python
from cohesity_sdk.models.common_target_configuration import CommonTargetConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of CommonTargetConfiguration from a JSON string
common_target_configuration_instance = CommonTargetConfiguration.from_json(json)
# print the JSON string representation of the object
print(CommonTargetConfiguration.to_json())

# convert the object into a dict
common_target_configuration_dict = common_target_configuration_instance.to_dict()
# create an instance of CommonTargetConfiguration from a dict
common_target_configuration_from_dict = CommonTargetConfiguration.from_dict(common_target_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


