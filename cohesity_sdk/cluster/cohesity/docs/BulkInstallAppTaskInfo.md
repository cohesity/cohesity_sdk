# BulkInstallAppTaskInfo

Parameters for a bulk install app task.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str, none_type** | Job id of the bulk install app task. | [optional] 
**num_machines_failed** | **int, none_type** | Number of machines on which bulk install app task is failed. | [optional] 
**num_machines_passed** | **int, none_type** | Number of machines on which bulk install app task is passed. | [optional] 
**num_machines_total** | **int, none_type** | Number of machines on which bulk install app task is started. | [optional] 
**registering_app** | **str, none_type** | Application being registered. This param is used to indicate the app for which the job is created. &#39;oracle&#39; indicates that the job was created for oracle app. &#39;msSql&#39; indicates that the job was created for msSql app. &#39;physical&#39; indicates that the job was created for physical machine. | [optional] 
**state** | **str, none_type** | Current state of the task. This param is used to indicate the state of the job created by the bulk install app. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


