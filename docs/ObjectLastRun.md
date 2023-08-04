# ObjectLastRun

Specifies last run info of an object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | Specifies object id. | [optional] 
**name** | **str, none_type** | Specifies the name of the object. | [optional] 
**source_id** | **int, none_type** | Specifies registered source id to which object belongs. | [optional] 
**source_name** | **str, none_type** | Specifies registered source name to which object belongs. | [optional] 
**environment** | **str, none_type** | Specifies the environment of the object. | [optional] 
**object_hash** | **str, none_type** | Specifies the hash identifier of the object. | [optional] 
**object_type** | **str, none_type** | Specifies the type of the object. | [optional] 
**logical_size_bytes** | **int, none_type** | Specifies the logical size of object in bytes. | [optional] 
**uuid** | **str, none_type** | Specifies the uuid which is a unique identifier of the object. | [optional] 
**global_id** | **str, none_type** | Specifies the global id which is a unique identifier of the object. | [optional] 
**protection_type** | **str, none_type** | Specifies the protection type of the object if any. | [optional] 
**os_type** | **str, none_type** | Specifies the operating system type of the object. | [optional] 
**v_center_summary** | [**ObjectTypeVCenterParams**](ObjectTypeVCenterParams.md) |  | [optional] 
**sharepoint_site_summary** | [**SharepointObjectParams**](SharepointObjectParams.md) |  | [optional] 
**windows_cluster_summary** | [**ObjectTypeWindowsClusterParams**](ObjectTypeWindowsClusterParams.md) |  | [optional] 
**run_id** | **str** | Specifies the last run id. | [optional] 
**protection_group_name** | **str, none_type** | Specifies the protection group name of last run. | [optional] 
**protection_group_id** | **str, none_type** | Specifies the protection group id of last run. | [optional] 
**policy_name** | **str, none_type** | Specifies the policy name of last run. | [optional] 
**policy_id** | **str, none_type** | Specifies the policy id of last run. | [optional] 
**backup_run_status** | **str, none_type** | Specifies the status of last local back up run. | [optional] 
**archival_run_status** | **str, none_type** | Specifies the status of last archival run. | [optional] 
**replication_run_status** | **str, none_type** | Specifies the status of last replication run. | [optional] 
**is_sla_violated** | **bool, none_type** | Specifies if the sla is violated in last run. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


