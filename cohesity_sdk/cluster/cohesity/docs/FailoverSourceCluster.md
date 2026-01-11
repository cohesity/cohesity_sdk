# FailoverSourceCluster

Specifies the details about source cluster involved in the failover operation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | Specifies the source cluster Id involved in failover operation. | 
**incarnation_id** | **int, none_type** | Specifies the source cluster incarnation Id involved in failover operation. | [optional] [readonly] 
**protection_group_id** | **str, none_type** | Specifies the protection group Id involved in failover operation. | [optional] [readonly] 
**view_id** | **int, none_type** | If failover is initiated by view based orchastrator, then this field specifies the local view id of source cluster which is being failed over. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


