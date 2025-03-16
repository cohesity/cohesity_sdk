# McmObjectRecoverActivityParams

Specifies the Object activity of a recovery.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time_usecs** | **int** | Specifies the end time of the Recovery in Unix timestamp epoch in microseconds. This field will be populated only after Recovery is finished. | [optional] 
**id** | **str** | Specifies the id of the Recovery. | [optional] 
**name** | **str** | Specifies the name of the Recovery. | [optional] 
**progress_task_id** | **str** | Progress monitor task id for Recovery. | [optional] 
**recovery_type** | **str** | Specifies the recovery type. | [optional] 
**snapshot_creation_time_usecs** | **int** | Specifies the time when the snapshot is created in Unix timestamp epoch in microseconds. | [optional] [readonly] 
**start_time_usecs** | **int** | Specifies the start time of the Recovery in Unix timestamp epoch in microseconds. | [optional] 
**status** | **str** | Status of the Recovery. &#39;Running&#39; indicates that the Recovery is still running. &#39;Canceled&#39; indicates that the Recovery has been cancelled. &#39;Canceling&#39; indicates that the Recovery is in the process of being cancelled. &#39;Failed&#39; indicates that the Recovery has failed. &#39;Succeeded&#39; indicates that the Recovery has finished successfully. &#39;SucceededWithWarning&#39; indicates that the Recovery finished successfully, but there were some warning messages. &#39;Skipped&#39; indicates that the run was skipped. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_object_recover_activity_params import McmObjectRecoverActivityParams

# TODO update the JSON string below
json = "{}"
# create an instance of McmObjectRecoverActivityParams from a JSON string
mcm_object_recover_activity_params_instance = McmObjectRecoverActivityParams.from_json(json)
# print the JSON string representation of the object
print(McmObjectRecoverActivityParams.to_json())

# convert the object into a dict
mcm_object_recover_activity_params_dict = mcm_object_recover_activity_params_instance.to_dict()
# create an instance of McmObjectRecoverActivityParams from a dict
mcm_object_recover_activity_params_from_dict = McmObjectRecoverActivityParams.from_dict(mcm_object_recover_activity_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


