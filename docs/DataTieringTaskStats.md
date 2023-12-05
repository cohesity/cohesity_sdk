# DataTieringTaskStats

Specifies the stats of data tiering task.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes_read** | **int, none_type** | Specifies total logical bytes read for creating the snapshot. | [optional] 
**bytes_written** | **int, none_type** | Specifies total size of data in bytes written after taking backup. | [optional] 
**logical_size_bytes** | **int, none_type** | Specifies total logical size of object(s) in bytes. | [optional] 
**changed_entity_count** | **int, none_type** | Specifies changed entity count. | [optional] 
**entity_count** | **int, none_type** | Specifies total entity count. | [optional] 
**is_tiering_goal_met** | **bool, none_type** | Specifies whether tiering goal has been met. | [optional]  if omitted the server will use the default value of False
**total_tiered_bytes** | **int, none_type** | Specifies total amount of data successfully tiered from the NAS source. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


