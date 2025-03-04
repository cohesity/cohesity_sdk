# ReplicationTargetProgressInfo

Specifies the progress of a replication run target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Specifies the id of the cluster. | [optional] 
**cluster_incarnation_id** | **int** | Specifies the incarnation id of the cluster. | [optional] 
**cluster_name** | **str** | Specifies the name of the cluster. | [optional] [readonly] 
**aws_target_config** | [**AWSTargetConfig**](AWSTargetConfig.md) |  | [optional] 
**azure_target_config** | [**AzureTargetConfig**](AzureTargetConfig.md) |  | [optional] 
**end_time_usecs** | **int** | Specifies the end time of the progress task in Unix epoch Timestamp(in microseconds). | [optional] 
**events** | [**List[ProgressTaskEvent]**](ProgressTaskEvent.md) | Specifies the event log created for progress Task. | [optional] 
**expected_remaining_time_usecs** | **int** | Specifies the expected remaining time of the progress task in Unix epoch Timestamp(in microseconds). | [optional] 
**percentage_completed** | **float** | Specifies the current completed percentage of the progress task. | [optional] 
**start_time_usecs** | **int** | Specifies the start time of the progress task in Unix epoch Timestamp(in microseconds). | [optional] 
**stats** | [**ProgressStats**](ProgressStats.md) |  | [optional] 
**status** | **str** | Specifies the current status of the progress task. | [optional] 
**objects** | [**List[ObjectProgressInfo]**](ObjectProgressInfo.md) | Specifies progress for objects. | [optional] 

## Example

```python
from cohesity_sdk.models.replication_target_progress_info import ReplicationTargetProgressInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationTargetProgressInfo from a JSON string
replication_target_progress_info_instance = ReplicationTargetProgressInfo.from_json(json)
# print the JSON string representation of the object
print(ReplicationTargetProgressInfo.to_json())

# convert the object into a dict
replication_target_progress_info_dict = replication_target_progress_info_instance.to_dict()
# create an instance of ReplicationTargetProgressInfo from a dict
replication_target_progress_info_from_dict = ReplicationTargetProgressInfo.from_dict(replication_target_progress_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


