# ObjectStatsInfo

Specifies the Stats of an object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | [**ObjectStringIdentifier**](ObjectStringIdentifier.md) |  | [optional] 
**environment** | **str, none_type** | Specifies the environment of the object. | [optional] 
**id** | **int, none_type** | Specifies object id. | [optional] 
**name** | **str, none_type** | Specifies the name of the object. | [optional] 
**source_id** | **int, none_type** | Specifies registered source id to which object belongs. | [optional] 
**source_name** | **str, none_type** | Specifies registered source name to which object belongs. | [optional] 
**backup_generic_stats** | [**BackupGenericStats**](BackupGenericStats.md) |  | [optional] 
**nas_stats** | [**BackupNasStats**](BackupNasStats.md) |  | [optional] 
**failed_attempts** | [**[StatsTaskInfo], none_type**](StatsTaskInfo.md) | Specifies stats for failed attempts of this object. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


