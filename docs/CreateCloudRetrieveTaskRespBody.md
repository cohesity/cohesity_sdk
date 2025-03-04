# CreateCloudRetrieveTaskRespBody

Specifies the response to create cloud retrieve tasks.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**progress_task_id** | **int** | Specifies the progress task id. | [optional] 
**retrieve_job_id** | **str** | Specifies the cloud retrieve job Id | [optional] 

## Example

```python
from cohesity_sdk.models.create_cloud_retrieve_task_resp_body import CreateCloudRetrieveTaskRespBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCloudRetrieveTaskRespBody from a JSON string
create_cloud_retrieve_task_resp_body_instance = CreateCloudRetrieveTaskRespBody.from_json(json)
# print the JSON string representation of the object
print(CreateCloudRetrieveTaskRespBody.to_json())

# convert the object into a dict
create_cloud_retrieve_task_resp_body_dict = create_cloud_retrieve_task_resp_body_instance.to_dict()
# create an instance of CreateCloudRetrieveTaskRespBody from a dict
create_cloud_retrieve_task_resp_body_from_dict = CreateCloudRetrieveTaskRespBody.from_dict(create_cloud_retrieve_task_resp_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


