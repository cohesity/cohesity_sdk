# SupportChannelConfig

Specifies the support channel configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time_usecs** | **int, none_type** | Specifies the support channel expiry time. | 
**is_enabled** | **bool, none_type** | Specifies if the support channel should be enabled. | 
**enable_extension** | **bool, none_type** | Specifies if the support channel extension is allowed. | [optional] 
**extension_duration_hours** | **int, none_type** | Specifies the support channel extension duration in hours. | [optional] 
**force_enable_reverse_tunnel** | **bool** | Specifies if SSH reverse tunnel should be initiated with RT server. Use this only if there are connectivity issues with Support Channel server. | [optional] 
**node_ids** | **[int], none_type** | List of nodes where support channel should be enabled in addition to master node. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


