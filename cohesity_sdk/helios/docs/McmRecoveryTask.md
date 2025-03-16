# McmRecoveryTask

Specifies the recovery task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Specifies the cluster id. | [optional] 
**cluster_incarnation_id** | **int** | Specifies the cluster incarnation id. | [optional] 
**cluster_name** | **str** | Specifies the cluster name. | [optional] 
**end_time_usecs** | **int** | Specifies the end time of the Recovery in Unix timestamp epoch in microseconds. This field will be populated only after Recovery is finished. | [optional] 
**id** | **str** | Specifies the id of the Recovery. | [optional] 
**name** | **str** | Specifies the name of the Recovery. | [optional] 
**progress_task_id** | **str** | Progress monitor task id for Recovery. | [optional] 
**recovery_action** | **str** | Specifies the recovery action. | [optional] 
**region_id** | **str** | Specifies the region id where the cluster is located for DMaaS. | [optional] [readonly] 
**rpaas_global_vault_id** | **str** | Specifies FortKnox global vault id. | [optional] [readonly] 
**rpaas_region_id** | **str** | Specifies the region id where the snapshots are from to perform the recovery. This is only for RPaaS. | [optional] [readonly] 
**snapshot_environment** | **str** | Specifies the snapshot environment. | [optional] 
**start_time_usecs** | **int** | Specifies the start time of the Recovery in Unix timestamp epoch in microseconds. | [optional] 
**status** | **str** | Status of the Recovery. &#39;Running&#39; indicates that the Recovery is still running. &#39;Canceled&#39; indicates that the Recovery has been cancelled. &#39;Canceling&#39; indicates that the Recovery is in the process of being cancelled. &#39;Failed&#39; indicates that the Recovery has failed. &#39;Succeeded&#39; indicates that the Recovery has finished successfully. &#39;SucceededWithWarning&#39; indicates that the Recovery finished successfully, but there were some warning messages. &#39;Skipped&#39; indicates that the Recovery task was skipped. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_recovery_task import McmRecoveryTask

# TODO update the JSON string below
json = "{}"
# create an instance of McmRecoveryTask from a JSON string
mcm_recovery_task_instance = McmRecoveryTask.from_json(json)
# print the JSON string representation of the object
print(McmRecoveryTask.to_json())

# convert the object into a dict
mcm_recovery_task_dict = mcm_recovery_task_instance.to_dict()
# create an instance of McmRecoveryTask from a dict
mcm_recovery_task_from_dict = McmRecoveryTask.from_dict(mcm_recovery_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


