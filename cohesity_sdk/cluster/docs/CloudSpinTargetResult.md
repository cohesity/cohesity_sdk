# CloudSpinTargetResult

Cloud Spin result for a target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_params** | [**AwsCloudSpinParams**](AwsCloudSpinParams.md) |  | [optional] 
**azure_params** | [**AzureCloudSpinParams**](AzureCloudSpinParams.md) |  | [optional] 
**id** | **int** | Specifies the unique id of the cloud spin entity. | [optional] 
**name** | **str** | Specifies the name of the already added cloud spin target. | [optional] [readonly] 
**cloudspin_task_id** | **str** | Task ID for a CloudSpin protection run. | [optional] 
**data_lock_constraints** | [**DataLockConstraints**](DataLockConstraints.md) |  | [optional] 
**end_time_usecs** | **int** | Specifies the end time of Cloud Spin in Unix epoch Timestamp(in microseconds) for a target. | [optional] 
**expiry_time_usecs** | **int** | Specifies the expiry time of attempt in Unix epoch Timestamp (in microseconds) for an object. | [optional] 
**is_manually_deleted** | **bool** | Specifies whether the snapshot is deleted manually. | [optional] 
**message** | **str** | Message about the Cloud Spin run. | [optional] 
**on_legal_hold** | **bool** | Specifies the legal hold status for a cloud spin target. | [optional] 
**progress_task_id** | **str** | Progress monitor task id for Cloud Spin run. | [optional] 
**start_time_usecs** | **int** | Specifies the start time of Cloud Spin in Unix epoch Timestamp(in microseconds) for a target. | [optional] 
**stats** | [**CloudSpinDataStats**](CloudSpinDataStats.md) |  | [optional] 
**status** | **str** | Status of the Cloud Spin for a target. &#39;Running&#39; indicates that the run is still running. &#39;Canceled&#39; indicates that the run has been canceled. &#39;Canceling&#39; indicates that the run is in the process of being canceled. &#39;Paused&#39; indicates that the ongoing run has been paused. &#39;Failed&#39; indicates that the run has failed. &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening. &#39;Succeeded&#39; indicates that the run has finished successfully. &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages. &#39;Skipped&#39; indicates that the run was skipped. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cloud_spin_target_result import CloudSpinTargetResult

# TODO update the JSON string below
json = "{}"
# create an instance of CloudSpinTargetResult from a JSON string
cloud_spin_target_result_instance = CloudSpinTargetResult.from_json(json)
# print the JSON string representation of the object
print(CloudSpinTargetResult.to_json())

# convert the object into a dict
cloud_spin_target_result_dict = cloud_spin_target_result_instance.to_dict()
# create an instance of CloudSpinTargetResult from a dict
cloud_spin_target_result_from_dict = CloudSpinTargetResult.from_dict(cloud_spin_target_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


