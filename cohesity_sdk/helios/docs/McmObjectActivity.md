# McmObjectActivity

Specifies the Object activity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Specifies the unique id of the activity event. | [optional] 
**object** | [**ObjectSummary**](ObjectSummary.md) |  | [optional] 
**source_info** | [**ObjectSummary**](ObjectSummary.md) |  | [optional] 
**cluster_id** | **int, none_type** | Specifies the cluster id. | [optional] [readonly] 
**cluster_incarnation_id** | **int, none_type** | Specifies the cluster incarnation id. | [optional] [readonly] 
**region_id** | **str, none_type** | Specifies the region id. Applicable only in case of DMaaS. | [optional] [readonly] 
**timestamp_usecs** | **int, none_type** | Specifies the timestamp in Unix timestamp epoch in microseconds at which this activity occured. | [optional] 
**type** | **str, none_type** | Specifies the type of activity event. | [optional] 
**backup_run_params** | [**McmObjectBackupRunActivityParams**](McmObjectBackupRunActivityParams.md) |  | [optional] 
**recovery_params** | [**McmObjectRecoverActivityParams**](McmObjectRecoverActivityParams.md) |  | [optional] 
**archival_run_params** | [**McmObjectArchivalRunActivityParams**](McmObjectArchivalRunActivityParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


