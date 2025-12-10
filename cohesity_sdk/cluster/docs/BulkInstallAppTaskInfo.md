# BulkInstallAppTaskInfo

Parameters for a bulk install app task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Job id of the bulk install app task. | [optional] 
**num_machines_failed** | **int** | Number of machines on which bulk install app task is failed. | [optional] 
**num_machines_passed** | **int** | Number of machines on which bulk install app task is passed. | [optional] 
**num_machines_total** | **int** | Number of machines on which bulk install app task is started. | [optional] 
**registering_app** | **str** | Application being registered. This param is used to indicate the app for which the job is created. &#39;oracle&#39; indicates that the job was created for oracle app. &#39;msSql&#39; indicates that the job was created for msSql app. &#39;physical&#39; indicates that the job was created for physical machine. | [optional] 
**state** | **str** | Current state of the task. This param is used to indicate the state of the job created by the bulk install app. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.bulk_install_app_task_info import BulkInstallAppTaskInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BulkInstallAppTaskInfo from a JSON string
bulk_install_app_task_info_instance = BulkInstallAppTaskInfo.from_json(json)
# print the JSON string representation of the object
print(BulkInstallAppTaskInfo.to_json())

# convert the object into a dict
bulk_install_app_task_info_dict = bulk_install_app_task_info_instance.to_dict()
# create an instance of BulkInstallAppTaskInfo from a dict
bulk_install_app_task_info_from_dict = BulkInstallAppTaskInfo.from_dict(bulk_install_app_task_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


