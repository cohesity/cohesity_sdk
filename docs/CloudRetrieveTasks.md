# CloudRetrieveTasks

List of cloud retrieve tasks.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retrieve_tasks** | [**List[CloudRetrieveTask]**](CloudRetrieveTask.md) | Specifies the list of cloud retrieve tasks. | [optional] 

## Example

```python
from cohesity_sdk.models.cloud_retrieve_tasks import CloudRetrieveTasks

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRetrieveTasks from a JSON string
cloud_retrieve_tasks_instance = CloudRetrieveTasks.from_json(json)
# print the JSON string representation of the object
print(CloudRetrieveTasks.to_json())

# convert the object into a dict
cloud_retrieve_tasks_dict = cloud_retrieve_tasks_instance.to_dict()
# create an instance of CloudRetrieveTasks from a dict
cloud_retrieve_tasks_from_dict = CloudRetrieveTasks.from_dict(cloud_retrieve_tasks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


