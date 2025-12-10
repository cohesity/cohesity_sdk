# BackupTaskInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **str** | Id of that particular Backup Task. | [optional] 
**name** | **str** | Name of the Backup task. | [optional] 
**start_time_usecs** | **str** | Denotes the start time of the backuptask, needed for deeplinking. | [optional] 
**task_id** | **str** | Id of the Backup task. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.backup_task_info import BackupTaskInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BackupTaskInfo from a JSON string
backup_task_info_instance = BackupTaskInfo.from_json(json)
# print the JSON string representation of the object
print(BackupTaskInfo.to_json())

# convert the object into a dict
backup_task_info_dict = backup_task_info_instance.to_dict()
# create an instance of BackupTaskInfo from a dict
backup_task_info_from_dict = BackupTaskInfo.from_dict(backup_task_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


