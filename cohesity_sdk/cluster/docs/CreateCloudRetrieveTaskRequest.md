# CreateCloudRetrieveTaskRequest

Specifies create cloud retrieve task request parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Specifies the cluster ID. | [optional] 
**end_time_usecs** | **int** | Specifies the end time in microseconds and filter the tasks by the end time. | [optional] 
**job_ids** | **List[str]** | Job ids to retrieve. | [optional] 
**retrieve_all_jobs** | **bool** | Specifies whether to retrieve all tasks. | [optional] 
**start_time_usecs** | **int** | Specifies the start time in microseconds and filter the task by the start time. | [optional] 
**vault_ids** | **List[int]** | Specifies the array of vault IDs. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.create_cloud_retrieve_task_request import CreateCloudRetrieveTaskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCloudRetrieveTaskRequest from a JSON string
create_cloud_retrieve_task_request_instance = CreateCloudRetrieveTaskRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCloudRetrieveTaskRequest.to_json())

# convert the object into a dict
create_cloud_retrieve_task_request_dict = create_cloud_retrieve_task_request_instance.to_dict()
# create an instance of CreateCloudRetrieveTaskRequest from a dict
create_cloud_retrieve_task_request_from_dict = CreateCloudRetrieveTaskRequest.from_dict(create_cloud_retrieve_task_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


