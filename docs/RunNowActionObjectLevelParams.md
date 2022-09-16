# RunNowActionObjectLevelParams

Specifies the request parameters for RunNow action on a Protected object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | Specifies the ID of the object. | 
**name** | **str, none_type** | Specifies the name of the object. | [optional] [readonly] 
**take_local_snapshot_only** | **bool, none_type** | If sepcified as true then runNow will only take local snapshot ignoring all other targets such as replication, archivals etc. If not sepcified or specified as false then runNow will follow the policy settings. | [optional] 
**backup_type** | **str** | Specifies the backup type should be used for RunNow action. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


