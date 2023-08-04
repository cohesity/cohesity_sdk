# OnpremDeployConfig

Specifies the details about OnpremDeploy for snapshots.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule** | [**TargetSchedule**](TargetSchedule.md) |  | 
**retention** | [**Retention**](Retention.md) |  | 
**copy_on_run_success** | **bool, none_type** | Specifies if Snapshots are copied from the first completely successful Protection Group Run or the first partially successful Protection Group Run occurring at the start of the replication schedule. &lt;br&gt; If true, Snapshots are copied from the first Protection Group Run occurring at the start of the replication schedule that was completely successful i.e. Snapshots for all the Objects in the Protection Group were successfully captured. &lt;br&gt; If false, Snapshots are copied from the first Protection Group Run occurring at the start of the replication schedule, even if first Protection Group Run was not completely successful i.e. Snapshots were not captured for all Objects in the Protection Group. | [optional] 
**config_id** | **str, none_type** | Specifies the unique identifier for the target getting added. This field need to be passed only when policies are being updated. | [optional] 
**backup_run_type** | **str, none_type** | Specifies which type of run should be copied, if not set, all types of runs will be eligible for copying. If set, this will ensure that the first run of given type in the scheduled period will get copied. Currently, this can only be set to Full. | [optional] 
**params** | [**OnpremDeployParams**](OnpremDeployParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


