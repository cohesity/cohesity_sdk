# RecoverMongodbParamsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshots** | [**[RecoverMongodbSnapshotParams], none_type**](RecoverMongodbSnapshotParams.md) | Specifies the local snapshot ids of the Objects to be recovered. | 
**recover_user_roles** | **bool, none_type** | Specifies whether to recover User and roles at the time of recovery. | [optional] 
**recover_zones_tags** | **bool, none_type** | Specifies whether to recover Zones/shard tags at the time of recovery. | [optional] 
**suffix** | **str, none_type** | A suffix that is to be applied to all recovered objects. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


