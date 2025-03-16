# RetrieveArchiveTask

Specifies the persistent state of a retrieve of an archive task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_uid** | **str** | Specifies the globally unique id for this retrieval of an archive task. | [optional] 
**uptier_expiry_times** | **List[int]** | Specifies how much time the retrieved entity is present in the hot-tiers. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.retrieve_archive_task import RetrieveArchiveTask

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveArchiveTask from a JSON string
retrieve_archive_task_instance = RetrieveArchiveTask.from_json(json)
# print the JSON string representation of the object
print(RetrieveArchiveTask.to_json())

# convert the object into a dict
retrieve_archive_task_dict = retrieve_archive_task_instance.to_dict()
# create an instance of RetrieveArchiveTask from a dict
retrieve_archive_task_from_dict = RetrieveArchiveTask.from_dict(retrieve_archive_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


