# CassandraParams

Specifies the recovery options specific to Cassandra environment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_cassandra_params** | [**RecoverCassandraParams**](RecoverCassandraParams.md) |  | 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | defaults to "RecoverObjects"
**continue_on_error** | **bool, none_type** | Specifies whether to continue recovering other objects if one of Object failed to recover. Default value is false. | [optional] 
**is_multi_stage_restore** | **bool, none_type** | Specifies whether the current recovery operation is a multi-stage restore operation. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


