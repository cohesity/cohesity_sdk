# ArchivalTargetStatsInfo

Specifies the stats of an archival run target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_id** | **int, none_type** | Specifies the archival target ID. | [optional] 
**archival_task_id** | **str, none_type** | Specifies the archival task id. This is a protection group UID which only applies when archival type is &#39;Tape&#39;. | [optional] 
**target_name** | **str, none_type** | Specifies the archival target name. | [optional] 
**target_type** | **str, none_type** | Specifies the archival target type. | [optional] 
**usage_type** | **str, none_type** | Specifies the usage type for the target. | [optional] 
**ownership_context** | **str, none_type** | Specifies the ownership context for the target. | [optional] 
**tier_settings** | [**ArchivalTargetTierInfo**](ArchivalTargetTierInfo.md) |  | [optional] 
**backup_generic_stats** | [**BackupGenericStats**](BackupGenericStats.md) |  | [optional] 
**nas_stats** | [**BackupNasStats**](BackupNasStats.md) |  | [optional] 
**objects** | [**[ObjectStatsInfo], none_type**](ObjectStatsInfo.md) | Specifies stats for objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


