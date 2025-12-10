# ReplicationTargetInfo

Simplified replication target result with essential fields only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_name** | **str** | Specifies the name of the cluster. | [optional] [readonly] 
**end_time_usecs** | **int** | Specifies the end time of replication in Unix epoch Timestamp(in microseconds) for a target. | [optional] 
**queued_time_usecs** | **int** | Specifies the time when the replication is queued for schedule in Unix epoch Timestamp(in microseconds) for a target. | [optional] 
**start_time_usecs** | **int** | Specifies the start time of replication in Unix epoch Timestamp(in microseconds) for a target. | [optional] 
**stats** | [**ReplicationDataStats**](ReplicationDataStats.md) |  | [optional] 
**status** | **str** | Status of the replication for a target. &#39;Running&#39; indicates that the run is still running. &#39;Canceled&#39; indicates that the run has been canceled. &#39;Canceling&#39; indicates that the run is in the process of being canceled. &#39;Paused&#39; indicates that the ongoing run has been paused. &#39;Failed&#39; indicates that the run has failed. &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening. &#39;Succeeded&#39; indicates that the run has finished successfully. &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages. &#39;Skipped&#39; indicates that the run was skipped. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.replication_target_info import ReplicationTargetInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationTargetInfo from a JSON string
replication_target_info_instance = ReplicationTargetInfo.from_json(json)
# print the JSON string representation of the object
print(ReplicationTargetInfo.to_json())

# convert the object into a dict
replication_target_info_dict = replication_target_info_instance.to_dict()
# create an instance of ReplicationTargetInfo from a dict
replication_target_info_from_dict = ReplicationTargetInfo.from_dict(replication_target_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


